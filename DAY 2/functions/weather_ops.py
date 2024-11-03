import requests
import json

def get_weather(city: str) -> str:
    try:
        geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geocoding_url)
        geo_data = geo_response.json()
        
        if not geo_data.get('results'):
            return json.dumps({
                "status": "error",
                "message": f"City '{city}' not found"
            })
            
        location = geo_data['results'][0]
        lat, lon = location['latitude'], location['longitude']
        
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        current = weather_data['current']
        
        return json.dumps({
            "status": "success",
            "location": location['name'],
            "country": location['country'],
            "temperature": f"{current['temperature_2m']}°C",
            "humidity": f"{current['relative_humidity_2m']}%",
            "wind_speed": f"{current['wind_speed_10m']} km/h",
            "message": f"Current weather in {location['name']}, {location['country']}"
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })