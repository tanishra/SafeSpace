import re

def clean_text(text):
    if not isinstance(text, str):
        text = str(text)  # Defensive: convert non-string input

    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Convert hashtags to plain words
    text = re.sub(r"#([A-Za-z0-9_]+)", r"\1", text)
    # Remove unwanted characters but keep letters, digits, spaces, basic punctuation
    text = re.sub(r"[^a-zA-Z0-9\s.,!?'-]", "", text)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()
