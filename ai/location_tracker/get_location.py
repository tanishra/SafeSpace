import geocoder
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')


def get_current_location(api_key):
    """
    Fetch the user's current location using IP and Google Maps Reverse Geocoding API.
    
    Args:
        api_key (str): Your Google Maps API key.
    
    Returns:
        dict: Location details including latitude, longitude, city, state, country, and postal code.
    """
    # Step 1: Get current latitude and longitude using IP-based geolocation
    g = geocoder.ip('me')
    latlng = g.latlng

    if latlng:
        latitude, longitude = latlng
        print(f"Latitude: {latitude}, Longitude: {longitude}")

        # Step 2: Reverse geocode using Google Maps API
        geocode_url = (
            f"https://maps.googleapis.com/maps/api/geocode/json?"
            f"latlng={latitude},{longitude}&key={api_key}"
        )
        response = requests.get(geocode_url)
        data = response.json()

        if data['status'] == 'OK':
            results = data.get('results', [])
            if results:
                address_components = results[0].get('address_components', [])

                # Helper function to extract component by type
                def get_component(components, component_type):
                    for component in components:
                        if component_type in component['types']:
                            return component['long_name']
                    return 'Unknown'

                city = get_component(address_components, 'locality')
                state = get_component(address_components, 'administrative_area_level_1')
                country = get_component(address_components, 'country')
                postal_code = get_component(address_components, 'postal_code')

                # Create the result dictionary
                location_info = {
                    'latitude': latitude,
                    'longitude': longitude,
                    'city': city,
                    'state': state,
                    'country': country,
                    'postal_code': postal_code
                }

                return location_info
            else:
                print("No results found from reverse geocoding.")
        else:
            print("Error from Google API:", data['status'])
    else:
        print("Unable to determine location from IP.")

    # Return None if anything fails
    return None
