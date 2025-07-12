# test_ai_pipeline_demo.py

import sys
import os

# Add your project path
sys.path.append('/Users/tanishrajput/Desktop/SafeSpace')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai.nlp_engine.preprocess_text import clean_text
from ai.nlp_engine.extract_cities import extract_places
from ai.geo_matcher.location_matcher import is_threat_near_user


# --------------------------
# MOCKED DATA AND UTILITIES
# --------------------------

# Simulated user location: Connaught Place
user_coords = (28.6315, 77.2167)

# Demo news articles
demo_articles = [
    {
        "title": "Violent protest erupts near Connaught Place",
        "description": "A group of protestors turned violent causing injuries and chaos in the central Delhi area."
    },
    {
        "title": "Fire breaks out in Noida Sector 18 mall",
        "description": "Massive fire reported at a shopping center, rescue operations underway."
    },
    {
        "title": "Peace rally held in South Delhi",
        "description": "Citizens gathered for a peaceful demonstration supporting climate action."
    },
    {
        "title": "Tech event planned in Gurugram",
        "description": "Major IT companies will participate in a showcase next weekend."
    },
    {
        "title": "Tree planting drive in Pune",
        "description": "Environmentalists gathered to plant trees and raise awareness in Pune."
    }
]

# Mock CITY_COORDS
CITY_COORDS = {
    "Connaught Place": (28.6315, 77.2167),
    "Delhi": (28.6139, 77.2090),
    "North Delhi": (28.7090, 77.1325),
    "South Delhi": (28.4973, 77.1872),
    "Noida": (28.5355, 77.3910),
    "Noida Sector 18": (28.5700, 77.3250),
    "Gurugram": (28.4595, 77.0266),
    "Pune": (18.5204, 73.8567)
}

# Mock get_coordinates
def get_coordinates(place):
    return CITY_COORDS.get(place)

# Mock fetch_user_location
def fetch_user_location():
    return user_coords, "Connaught Place"

# --------------------------
# ANALYSIS FUNCTION
# --------------------------

def analyze_news_by_location(location):
    user_coords, _ = fetch_user_location()
    articles = demo_articles[:20]
    processed = []
    threat_flag = False

    for article in articles:
        title = article.get("title", "")
        desc = article.get("description", "")
        full_text = clean_text(f"{title} {desc}")
        print(full_text)
        places = extract_places(full_text)
        print(f"Extracted places from '{title}': {places}")

        is_near_threat = False
        threat_label = "No Threat"
        threat_score = 0
        distance_info = None
        reason = "No location detected in the article."

        for place in places:
            threat_coords = get_coordinates(place)
            if threat_coords:
                near, confidence, threat_class, distance_or_reason = is_threat_near_user(
                    user_coords, threat_coords, full_text, max_km=10
                )

                if near:
                    is_near_threat = True
                    threat_label = threat_class
                    threat_score = confidence
                    distance_info = distance_or_reason
                    reason = "Threat is within range."
                    break
                else:
                    threat_label = threat_class
                    threat_score = confidence
                    reason = distance_or_reason
                    if isinstance(distance_or_reason, (int, float)):
                        distance_info = round(distance_or_reason, 2)

        if is_near_threat:
            threat_flag = True

        processed.append({
            "title": title,
            "description": desc,
            "label": threat_label,
            "score": threat_score,
            "entities": places,
            "distance_km": distance_info,
            "reason": reason
        })

    return {
        "location": location,
        "threat": threat_flag,
        "articles": processed
    }

# --------------------------
# RUN THE TEST
# --------------------------

if __name__ == "__main__":
    result = analyze_news_by_location("Delhi")

    print("\n🚨 Threat Detected:", result["threat"])
    print("\n📄 Analyzed Articles:")
    for article in result["articles"]:
        print("\n-------------------------------------")
        print(f"Title: {article['title']}")
        print(f"Label: {article['label']}")
        print(f"Confidence: {article['score']}%")
        print(f"Entities: {article['entities']}")
        print(f"Distance: {article['distance_km']} km")
        print(f"Reason: {article['reason']}")
