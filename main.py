import urllib.request
import json
import sys

city = input("Enter city: ")

# API Key و URL پایه
api_key = "6KFYM86MH87VLGW36Y4H7XB2A"
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&include=days&key={api_key}&contentType=json"

try:
  
    with urllib.request.urlopen(url) as response:
        jsonData = json.load(response)
        
    
        print(json.dumps(jsonData, indent=4))
except urllib.error.HTTPError as e:
    error_info = e.read().decode()
    print('Error code:', e.code, error_info)
    sys.exit()
except urllib.error.URLError as e:
    print('Error:', e.reason)
    sys.exit()
