import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ.get("apikey")
print(apikey)

url_base = "http://www.omdbapi.com/?"

url = url_base + str(apikey) + "&i=tt3896198"

print(url)
