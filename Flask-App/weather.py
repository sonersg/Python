

# python3 -m venv .venv
# source .venv/bin/activate
# pip install requests Flask python-dotenv
# pip freeze > requirements.txt

from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="istanbul"):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions *** \n")
    city = input("\nPlease enter a city name: \n")
    # Check for empty strings and only spaces
    if not bool(city.strip()):
        city = "istanbul"
    weather_data = get_current_weather(city)
    pprint(weather_data)
