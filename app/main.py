from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_KEY = "0f7184241768f28209b040e9a56e112f"

@app.get("/weather/{city}")
def get_weather(city: str):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric&lang=ru"
    )

    r = requests.get(url)
    data = r.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    }

print(get_weather("Kolchugino"))