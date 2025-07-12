import logging
from typing import Dict, Any, List, Tuple, Union

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


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def analyze_news_by_location(location: str, max_articles: int = 20, threat_distance_km: int = 10) -> Dict[str, Any]:
    """
    Analyze the latest news articles for threats near a user's location.

    Args:
        location (str): The location to fetch news about.
        max_articles (int): Max number of news articles to process.
        threat_distance_km (int): Max distance (km) to consider a threat near user.

    Returns:
        Dict[str, Any]: Analysis results including threat flags and detailed article info.
    """
    try:
        user_coords, user_location_name = fetch_user_location()
        logger.info(f"User coordinates: {user_coords}, Location: {user_location_name}")
    except Exception as e:
        logger.error(f"Failed to fetch user location: {e}")
        return {
            "error": "Failed to fetch user location",
            "details": str(e),
        }

    try:
        articles = fetch_latest_news(location)[:max_articles]
    except Exception as e:
        logger.error(f"Failed to fetch news articles: {e}")
        return {
            "error": "Failed to fetch news articles",
            "details": str(e),
        }

    processed_articles = []
    threat_detected = False

    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        combined_text = f"{title} {description}"

        cleaned_text = clean_text(combined_text)
        places = extract_places(cleaned_text)

        article_threat_flag = False
        threat_label = "No Threat"
        threat_score = 0.0
        distance_km = None
        threat_reason = "No location detected in the article."

        for place in places:
            threat_coords = get_coordinates(place)
            if not threat_coords:
                logger.debug(f"No coordinates found for place: {place}")
                continue

            near, confidence, threat_class, distance_or_reason = is_threat_near_user(
                user_coords, threat_coords, cleaned_text, max_km=threat_distance_km
            )

            if near:
                article_threat_flag = True
                threat_label = threat_class
                threat_score = confidence
                distance_km = round(distance_or_reason, 2) if isinstance(distance_or_reason, (int, float)) else None
                threat_reason = "Threat is within range."
                break
            else:
                # When not near, distance_or_reason explains why
                threat_label = threat_class
                threat_score = confidence
                threat_reason = distance_or_reason
                if isinstance(distance_or_reason, (int, float)):
                    distance_km = round(distance_or_reason, 2)

        if article_threat_flag:
            threat_detected = True

        processed_articles.append({
            "title": title,
            "description": description,
            "cleaned_text": cleaned_text,
            "entities": places,
            "threat_label": threat_label,
            "threat_score": threat_score,
            "distance_km": distance_km,
            "threat_reason": threat_reason,
            "threat_detected": article_threat_flag,
        })

    return {
        "requested_location": location,
        "user_location": user_location_name,
        "user_coordinates": user_coords,
        "threat_detected": threat_detected,
        "article_count": len(processed_articles),
        "articles": processed_articles,
    }


if __name__ == "__main__":
    result = analyze_news_by_location("Delhi")

    print("\n🚨 Threat Detected:", result["threat_detected"])
    print("\n📄 Analyzed Articles:")
    for article in result["articles"]:
        print("\n-------------------------------------")
        print(f"Title: {article['title']}")
        print(f"Label: {article['threat_label']}")
        print(f"Confidence: {article['threat_score']}%")
        print(f"Entities: {article['entities']}")
        print(f"Distance: {article['distance_km']} km")
        print(f"Reason: {article['threat_reason']}")