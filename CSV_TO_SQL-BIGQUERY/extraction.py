import httpx
import asyncio
import json

async def fetch_weather(cities:dict, name:str):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":cities[name]["latitude"],  # Coordenadas de Bogotá
        "longitude": cities[name]["longitude"],
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        
        if response.status_code == 200:
#            print(response.json())  # Imprime la respuesta en formato JSON
            return response.json()
        else:
            print(f"Error: {response.status_code}")

#bogota = asyncio.run(fetch_weather(4.6097,-74.0817))


cities = {
    "bogota":{
        "latitude":4.6097,
        "longitude":-74.0817
        },
    "barranquilla":{
        "latitude": 10.9639,
        "longitude": -74.7964
        },
    "santa marta":{
        "latitude": 11.2408,
        "longitude": -74.1990
        },
        "medellin":{
    "latitude":6.2442,
    "longitude":-75.5812
    },
    "bucaramanga":{
        "latitude":7.1193,
        "longitude":-73.1227
        },
}

async def main():

    weather_data = {}

    for city in cities.keys():
        data = await fetch_weather(cities=cities,name=city)
        if data:
            weather_data[city] = data["hourly"]["time"], data["hourly"]["temperature_2m"], data["hourly"]["relative_humidity_2m"], data["hourly"]["wind_speed_10m"]
    
    with open("climatic_data.json", "w", encoding="utf-8") as json_file:
        json.dump(weather_data,json_file,indent=4,ensure_ascii=False)

    print("📄 Archivo convertido exitosamente a JSON")


asyncio.run(main())

#asyncio.run(fetch_weather(cities=cities,name="barranquilla"))


