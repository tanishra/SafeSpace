import geocoder
import requests
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
DEFAULT_API_KEY = os.getenv('GOOGLE_API_KEY')


def get_location(place_name=None, api_key=DEFAULT_API_KEY):
    """
    Get location details from either a place name or current IP-based location.

    Args:
        place_name (str, optional): Name of the city/place. If None, use IP location.
        api_key (str): Google Maps API key (default loaded from environment).

    Returns:
        dict: Location details including latitude, longitude, city, state, country, and postal code.
    """

    def extract_components(components):
        def get_component(component_type):
            for component in components:
                if component_type in component['types']:
                    return component['long_name']
            return 'Unknown'

        return {
            'city': get_component('locality'),
            'state': get_component('administrative_area_level_1'),
            'country': get_component('country'),
            'postal_code': get_component('postal_code'),
        }

    if place_name:
        # Forward geocoding
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key={api_key}"
    else:
        # Get coordinates from IP
        g = geocoder.ip('me')
        if not g.latlng:
            print("Unable to determine location from IP.")
            return None
        latitude, longitude = g.latlng
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"

    response = requests.get(geocode_url)
    data = response.json()

    if data['status'] == 'OK':
        results = data.get('results', [])
        if results:
            location = results[0]['geometry']['location']
            components = results[0].get('address_components', [])
            extracted = extract_components(components)

            return {
                'latitude': location['lat'],
                'longitude': location['lng'],
                **extracted
            }
        else:
            print("No results found from geocoding.")
    else:
        print("Error from Google API:", data['status'])

    return None


