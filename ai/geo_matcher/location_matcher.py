from geopy.distance import geodesic
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'threat_detection')))
from threat_detection import detect_threat


def is_threat_near_user(user_coords, threat_coords, threat_text, max_km=10):
    """
    Function to check if the threat is near the user (distance <= max_km) 
    and classify the threat based on the provided text.
    """
    # Calculate the distance between user and threat location
    distance = geodesic(user_coords, threat_coords).km

    # Classify the threat based on the text
    result = detect_threat([threat_text])[0]
    threat_class = result['threat_level']
    confidence = result['score_percent']

    if distance > max_km:
        return False, confidence, threat_class, distance 
    if threat_class == "No Threat":
        return False, confidence, threat_class, distance

    # Threat is valid and within range
    distance = round(distance, 2)  
    return True, confidence, threat_class, distance