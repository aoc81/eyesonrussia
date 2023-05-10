# Eyes On Russia
This Python scripts collects the events that have been added to the [Russia-Ukraine Monitor Map](https://eyesonrussia.org/) made by Centre for Information Resilience (CIR), Bellingcat, Conflict Intelligence Team  and the wider open source community, and it produces an output as local JSON or Excel files. Aditionally, you could automatically store the data in your own Google Spreadsheet account.  

# Instructions
Make you have installed the required libraries and just execute the eyesonrussia.py script in your terminal and add any of the next optional arguments to filter the content and generate the output in your favorite format:
~~~
-- city "city name" 
-- date "YYYY-MM-DD"
-- country "country name"
-- latlon "lat,lon" // it accepts any coords length
-- format "extension" // it accepts json and xlsx
-- backup "gdrive" 
~~~

After proccessing the data and creating the file(s) you'll be asked if you also want to generates a Google Spreadsheet backup in your Google Drive account. 

ℹ️ If you want to proceed with this, you need firstly to insert your own client service keys in the file creds.json in order to make it work. 

## About the script
The intention of this repository is just to contribute with a small tool to produce an structured archive of the events that are happening and beeing verified by those organizations. For visualizations analysis, [Maphub](https://maphub.net) Eyes On Russia is a great resource, but data analysts might prefer to work directly with the data, or create a query to extract only certain events so I hope this script could be useful as it transforms this 👇

## About the author
I'm a Senior Webint Analyst but a beginner programmer so please feel free to clone this repository and improve it as much you want/need. Any contribution or suggestion would be more than welcome.  
