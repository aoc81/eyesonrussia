# Eyes On Russia
This Python scripts collects the events that have been added to the [Russia-Ukraine Monitor Map](https://eyesonrussia.org/) made by Centre for Information Resilience (CIR), Bellingcat, Conflict Intelligence Team  and the wider open source community, and it produces an output as local JSON or Excel files. Aditionally, you could automatically store the data in your own Google Spreadsheet account.  

# Instructions
Make you have installed the required libraries and just execute the eyesonrussia.py script in your terminal and add any of the next optional arguments to filter the content and generate the output in your favorite format:
~~~
eyesonrussia.py
-- city "city name" 
-- date "YYYY-MM-DD"
-- country "country name"
-- category "keyword" // for example: bombing, casualty, battle, detention, infrastructure, damage, military, etc
-- latlon "lat,lon" // it accepts any coords length
-- format "extension" // it accepts json and xlsx
-- backup "gdrive" 
~~~

After proccessing the data and creating the file(s) you'll be asked if you also want to generates a Google Spreadsheet backup in your Google Drive account. 

ℹ️ If you want to proceed with this, you need firstly to insert your own client service keys in the file creds.json in order to make it work. 

# Arguments Examples
Using arguments gives you the possibility to select and filter data based on your inputs, here you are examples:

`eyesonrussia.py --city "Mariupol" --category "firing" --format "json"`

`eyesonrussia.py --latlon "36.27,49.99" --date "2022-07-31" --format "xlsx`

# Output Examples
### Excel
![excel output](https://github.com/aoc81/eyesonrussia/assets/94049092/9118c74c-bd92-4517-9848-76057721498f)

### JSON
![image](https://github.com/aoc81/eyesonrussia/assets/94049092/6aea33e3-4483-4a6d-8b09-59310efa19bf)



# About the script
The intention of this repository is just to contribute with a small tool to produce an structured archive of the events that are happening and beeing verified by those organizations. For visualizations analysis, [Maphub](https://maphub.net) Eyes On Russia is a great resource, but data analysts might prefer to work directly with the data, or create a query to extract only certain events so I hope this script could be useful for some of you.

## About the author
I'm a Senior Webint Analyst but with basic code skills so please feel free to clone this repository and improve it as much you want/need. Any contribution or suggestion would be more than welcome.
