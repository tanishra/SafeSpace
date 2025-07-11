from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Local path to model
local_path = "/Users/tanishrajput/Desktop/SafeSpace/ai/threat_detection/threat_model"

# Load locally saved model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(local_path)
model = AutoModelForSequenceClassification.from_pretrained(local_path)

# Create pipeline using local model
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def get_threat_level(score_percent):
    if score_percent >= 90:
        return "High Threat"
    elif score_percent >= 75:
        return "Medium Threat"
    elif score_percent >= 50:
        return "Low Threat"
    else:
        return "No Threat"

# Function to detect threat and return structured list
def detect_threat(texts):
    results = []
    for text in texts:
        output = classifier(text)[0]  # Get top prediction
        score_percent = round(output["score"] * 100, 2)  # Convert to percentage
        threat_level = get_threat_level(score_percent)
        results.append({
            "text": text,
            "label": output["label"],
            "score_percent": f"{score_percent}%",
            "threat_level": threat_level
        })
    return results




