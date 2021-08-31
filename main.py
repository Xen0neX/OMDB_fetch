import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ.get("apikey")

url_base = "http://www.omdbapi.com/?apikey="

url = url_base + apikey + "&i=tt3896198"

print(url)

r = requests.get(url)
json_data = r.json()

for key, value in json_data.items():
    print(key + ':', value)
