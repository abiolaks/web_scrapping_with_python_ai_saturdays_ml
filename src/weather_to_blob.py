import requests
import pandas as pd
from datetime import datetime, timezone
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()

# Azure Blob details
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
CONTAINER_NAME = "weatherdata"

# OpenWeatherMap API details
API_KEY = os.getenv("weather_api_key")
NIGERIAN_CITIES = [
    "Lagos",
    "Abuja",
    "Kano",
    "Port Harcourt",
    "Ibadan",
    "Enugu",
    "Benin City",
    "Jos",
    "Kaduna",
    "Abeokuta",
]


def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},NG&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


def save_to_blob(file_path):
    blob_service_client = BlobServiceClient.from_connection_string(
        AZURE_CONNECTION_STRING
    )

    # Create container if it doesn't exist
    try:
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        container_client.create_container()
        print(f"✅ Created container: {CONTAINER_NAME}")
    except Exception as e:
        if "ContainerAlreadyExists" not in str(e):
            print(f"⚠️  Container creation info: {e}")

    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME, blob=os.path.basename(file_path)
    )
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"✅ Uploaded {file_path} to Azure Blob Storage.")


def main():
    # Check for required environment variables
    if not AZURE_CONNECTION_STRING:
        print("❌ Error: AZURE_CONNECTION_STRING environment variable not set")
        return

    if not API_KEY:
        print("❌ Error: weather_api_key environment variable not set")
        return

    data_list = []
    for city in NIGERIAN_CITIES:
        weather_data = fetch_weather(city)
        data_list.append(
            {
                "city": city,
                "country": weather_data.get("sys", {}).get("country"),
                "lat": weather_data.get("coord", {}).get("lat"),
                "lon": weather_data.get("coord", {}).get("lon"),
                "weather_main": weather_data.get("weather", [{}])[0].get("main"),
                "weather_description": weather_data.get("weather", [{}])[0].get(
                    "description"
                ),
                "temp": weather_data.get("main", {}).get("temp"),
                "feels_like": weather_data.get("main", {}).get("feels_like"),
                "temp_min": weather_data.get("main", {}).get("temp_min"),
                "temp_max": weather_data.get("main", {}).get("temp_max"),
                "pressure": weather_data.get("main", {}).get("pressure"),
                "humidity": weather_data.get("main", {}).get("humidity"),
                "visibility": weather_data.get("visibility"),
                "wind_speed": weather_data.get("wind", {}).get("speed"),
                "wind_deg": weather_data.get("wind", {}).get("deg"),
                "cloudiness": weather_data.get("clouds", {}).get("all"),
                "datetime": datetime.now(timezone.utc),
            }
        )

    df = pd.DataFrame(data_list)
    filename = f"nigeria_weather_{datetime.now(timezone.utc).strftime('%Y%m%d')}.csv"
    df.to_csv(filename, index=False)

    save_to_blob(filename)
    os.remove(filename)


if __name__ == "__main__":
    main()
