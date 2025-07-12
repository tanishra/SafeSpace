import os
import requests
import logging
from typing import Tuple, Optional
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_coordinates(city_name: str, retries: int = 3, timeout: int = 5) -> Optional[Tuple[float, float]]:
    """
    Fetches the latitude and longitude of a city using Google Geocoding API.

    Args:
        city_name (str): The name of the city to geocode.
        retries (int): Number of retry attempts for API call (default: 3).
        timeout (int): Timeout in seconds for the HTTP request (default: 5).

    Returns:
        Optional[Tuple[float, float]]: A tuple (latitude, longitude) if successful, else None.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logger.error("Google API key not found in environment variables.")
        return None

    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": city_name,
        "key": api_key
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(base_url, params=params, timeout=timeout)
            response.raise_for_status()
            data = response.json()

            if data.get("status") == "OK" and data["results"]:
                location = data["results"][0]["geometry"]["location"]
                lat, lng = location["lat"], location["lng"]
                logger.info(f"Coordinates for '{city_name}': ({lat}, {lng})")
                return lat, lng
            else:
                logger.warning(f"Geocoding API failed for '{city_name}': {data.get('status')}")
                return None

        except requests.RequestException as e:
            logger.error(f"Attempt {attempt}: Request failed for '{city_name}' - {e}")
            if attempt == retries:
                return None

    return None

