import sys
import os
sys.path.append('/Users/tanishrajput/Desktop/SafeSpace')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from ai.data_fetcher.fetch_news import fetch_latest_news
from ai.nlp_engine.preprocess_text import clean_text
from ai.nlp_engine.extract_cities import extract_places
from ai.geo_matcher.location_matcher import is_threat_near_user
from ai.location_tracker.get_threat_coordinates import get_coordinates
from app.services.geo_utils import fetch_user_location


def analyze_news_by_location(location):
    user_coords, _ = fetch_user_location()
    articles = fetch_latest_news(location)[:20]
    processed = []
    threat_flag = False

    for article in articles:
        title = article.get("title", "")
        desc = article.get("description", "")
        full_text = clean_text(f"{title} {desc}")

        places = extract_places(full_text)
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
                    distance_info = distance_or_reason  # It's a float when near is True
                    reason = "Threat is within range."
                    break
                else:
                    # It's a string when not near, explaining why
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