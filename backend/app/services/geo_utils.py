import sys
import os
import logging
from typing import Optional, Tuple, Dict
from dotenv import load_dotenv

# Update path to match your project structure
sys.path.append('/Users/tanishrajput/Desktop/SafeSpace')

# Import the updated get_location function
from ai.location_tracker.get_user_coordinates import get_location

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_user_location(place_name: Optional[str] = None) -> Tuple[Tuple[float, float], Optional[Dict[str, str]]]:
    """
    Fetch the user's geolocation (by IP or place name) and detailed address components.

    Args:
        place_name (Optional[str]): Name of a city/place. If None, IP-based location is used.

    Returns:
        Tuple:
            - (latitude, longitude) as a tuple of floats
            - Full location details (city, state, country, etc.) as a dictionary, or None if failed
    """
    location_info = get_location(place_name)

    if not location_info:
        logger.warning("Failed to retrieve location information.")
        return (0.0, 0.0), None

    latitude = location_info.get('latitude', 0.0)
    longitude = location_info.get('longitude', 0.0)

    logger.info(f"Coordinates: Latitude={latitude}, Longitude={longitude}")
    logger.debug(f"Location details: {location_info}")

    return (latitude, longitude), location_info



