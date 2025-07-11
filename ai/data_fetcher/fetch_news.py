import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to fetch the latest news
def fetch_latest_news(city):
    # Retrieve the API key from environment variables
    API_KEY = os.getenv("NEWS_API_KEY")
    
    if not API_KEY:
        print("API key is missing. Please make sure to set it in the .env file.")
        return []

    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={city}&language=en"
    
    headers = {
        "Accept": "application/json"
    }

    # Make the request to the API
    res = requests.get(url, headers=headers)

    # Check if the request was successful
    if res.status_code == 200:
        articles = res.json().get("results", [])
        
        # Get the first 10 articles (or fewer if less are available)
        latest_news = articles[:10]
        
        # Store the news articles in a list (with title and URL)
        news_list = [{"title": article["title"], "url": article["link"]} for article in latest_news]
        
        return news_list
    else:
        print(f"Error: {res.status_code}")
        return []
