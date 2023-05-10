# This script made by aoc81 is based on the Eyes on Russia Map data, which is a project from The Centre for Information Resilience
# For more info about the project, please visit https://eyesonrussia.org

import pandas as pd
import requests
import json
import time
import argparse

parser = argparse.ArgumentParser(description='Generates a JSON file with events data from a URL')
parser.add_argument('--city', type=str, help='Filter by city')
parser.add_argument('--date', type=str, help='Filter by date')
parser.add_argument('--country', type=str, help='Filter by country')
parser.add_argument('--category', type=str, help='Filter by category')
parser.add_argument('--latlon', type=str, help='Filter events by latitude and longitude (lat,lon)')
parser.add_argument('--format', type=str, choices=['json', 'excel'], default='json', help='Output file format (json or excel)')
args = parser.parse_args()


start_time = time.time()

# block for the request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0', 'Accept':'*/*','Content-Type':'application/json'}  
map_url = "https://eyesonrussia.org/events.geojson"
r = requests.get(map_url, headers=headers).json()

#structing response 
features = r['features']
events = []
for feature in features[0:-1]:
    try: 
        id = feature['properties']['id']
        date = feature['properties']['verifiedDate'][:10]
        url = feature['properties']['url']
        status = feature['properties']['status']
        credit = feature['properties']['credit']
        description = feature['properties']['description']
        country = feature['properties']['country']
        province = feature['properties']['province']
        district = feature['properties']['district']
        city = feature['properties']['city']
        latitude = feature['geometry']['coordinates'][0]
        longitude = feature['geometry']['coordinates'][1]
        category = feature['properties']['categories'][:]
    except:
        None

    event_details = {
        'id' : id,
        'date':date,
        'district': district,
        'city' : city,
        'province' : province, 
        'country':country,  
        'latitude': latitude, 
        'longitude': longitude,
        'source' : url,
        'status' : status,
        'credit' : credit,
        'categories' : category
        }
    events.append(event_details)
    
elapsed_time = time.time() - start_time

print("[*] Retrieving and reformating data based on your inputs... ")

#list comprehension to filter data based on given arguments
if args.city:
    events = [e for e in events if e['city'] == args.city]
if args.date:
    events = [e for e in events if e['date'] == args.date]
if args.country:
    events = [e for e in events if e['country'] == args.country]
if args.category:
    events = [e for e in events if any(args.category.lower() in c.lower() for c in e['categories'])]
if args.latlon:
    lat, lon = [round(float(coord.strip()), 1) for coord in args.latlon.split(',')]
    events = [e for e in events if abs(e['latitude'] - lat) <= 0.1 and abs(e['longitude'] - lon) <= 0.1]

# Generate output file with filtered events
if args.format == 'json':
    file_name = f"UWMaphub_events_filtered{'_' + args.city if args.city else ''}{'_' + args.date if args.date else ''}{'_' + args.country if args.country else ''}{'_' + args.category if args.category else ''}{'_' + args.latlon if args.latlon else ''}.json"
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(events, file, ensure_ascii=False, indent=4)
    print("[*] Operation has finished succesfully")
    print("[*]", len(events), f'events deta have been added to the file "UWMaphub_events.json" in {str(elapsed_time)[0:4]} seconds')
    
elif args.format == 'excel':
    file_name = f"UWMaphub_events_filtered{'_' + args.city if args.city else ''}{'_' + args.date if args.date else ''}{'_' + args.country if args.country else ''}{'_' + args.category if args.category else ''}{'_' + args.latlon if args.latlon else ''}.xlsx"
    df = pd.DataFrame(events)
    df.to_excel(file_name, index=False)
    print("[*] Operation has finished succesfully")
    print("[*]", len(events), f'events have been added to the file "UWMaphub_events.xlsx" in {str(elapsed_time)[0:4]} seconds')
