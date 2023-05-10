# Eyes On Russia
This Python script collects the events that have been added to the [Russia-Ukraine Monitor Map](https://eyesonrussia.org/) made by Centre for Information Resilience (CIR), Bellingcat, Conflict Intelligence Team  and the wider open source community, and it produces an output as local JSON or Excel files. Aditionally, you could automatically store the data in your own Google Spreadsheet account.  

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
-- backup "yes" // it creates a google spreadsheet on your google account. ℹ️ You need firstly to insert your own Google Sheet API keys in the file creds.json in order to make it work. 
~~~



# Arguments Examples
Using arguments gives you the possibility to select and filter data based on your inputs, here you are examples:

`python eyesonrussia.py --city "Mariupol" --category "damage" --format "json"`

`python eyesonrussia.py --latlon "36.27,49.99" --date "2022-07-31" --format "xlsx`

# Output Examples
### Excel
![excel output](https://i.imgur.com/qPPx9Jm.jpeg)

### JSON
![image](https://i.imgur.com/HRuOQlA.jpeg)



# About the script
The intention of this repository is just to contribute with a small tool to produce an structured archive of the events that are happening and beeing verified by those organizations. For visualizations analysis, [Eyes On Russia](https://eyesonrussia.org) is a great resource, but data analysts might prefer to work directly with the data, or create a query to extract only certain events so I hope this script could be useful for some of you.

## About the author
I'm a Senior Webint Analyst with basic code skills so please feel free to clone this repository and improve it as much you want/need. Any contribution or suggestion would be more than welcome.
