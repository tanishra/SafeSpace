import feedparser

EMERGENCY_FEEDS = [
    "https://ndma.gov.in/rss/emergency.xml",
    "https://mausam.imd.gov.in/rss/nowcast.xml" 
    # Add more if available
]

def fetch_emergency_feeds():
    entries = []
    for feed_url in EMERGENCY_FEEDS:
        feed = feedparser.parse(feed_url)
        entries.extend([entry.title for entry in feed.entries])
    return entries