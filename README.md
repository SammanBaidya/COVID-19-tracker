## COVID-19-tracker
Tracking COVID-19 in USA and worldwide.

### Project Overview: 
Description: A RESTful API that provides realtime COVID-19 statistics for the USA and worldwide. API allows users to access the data through specific endpoints.
## Technology Used:
Python, Flask, Docker, API developmen and Localtuneel for accessibility.

## TO setup:
1)Close the repo:
git clone <repository_url>
cd covid-tracker-api

2) Create a VM: (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:
pip intall -r requirements.txt 

4) Run the app:
python mains.py

#You cna access the COVID-19 tracket API using this link(valid for 7 days, I'll keep updating): https://fair-times-jog.loca.lt/
To test endpoints examples:
Get USA Statistics:
GET https://fair-times-jog.loca.lt/country/USA

Get Global Statistics:
GET https://fair-times-jog.loca.lt/global

#### More updates coming to include more countries, hosting in GCP, adding authentication, database to store data and 
compare monthly cases.....
