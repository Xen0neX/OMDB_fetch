import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ.get("apikey")

url_base = "http://www.omdbapi.com/?apikey="

title = input("Movie Name: ")
title = title.replace(" ", "_")

url = url_base + apikey + "&t=" + title

r = requests.get(url)
json_data = r.json()

#If you want to print all the data recieved from the API call
#for key, value in json_data.items():
#    print(key + ':', value)

print(json_data['imdbRating'])


