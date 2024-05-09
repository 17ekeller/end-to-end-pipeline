import requests
import json
from config import api_key

def rawExtractor() -> json:
    url = "https://api.weatherapi.com/v1/current.json?"
    apiKey = api_key
    params = {"key": apiKey, "q": "Chicago", "aqi": "no"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for non-2xx responses
        responseData = response.json()
    except Exception as e:
        print(f"Error: {e}")

    #Un-nesting the nested json data
    locationData = responseData.get("location", {})
    currentData = responseData.get("current", {})

    combined_data = {**locationData, **currentData} #concatonation of dictionaries
    rawDataFile = json.dumps(combined_data)

    return(rawDataFile)
