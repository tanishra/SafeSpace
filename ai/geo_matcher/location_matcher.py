from geopy.distance import geodesic
from transformers import pipeline
import torch 

device = torch.device('cpu')

local_model_path = "/Users/tanishrajput/Desktop/SafeSpace/ai/nlp_engine/bhadresh-bert-emotion-model"
classifier = pipeline("text-classification", model=local_model_path, tokenizer=local_model_path)

def detect_threat(text):
    result = classifier(text)[0]
    return result["label"], result["score"]


def classify_threat(text):
    """
    Function to classify a given threat text into emotional categories like 'anger', 'fear', etc.
    """
    label, score = detect_threat(text)
    if label == 'ANGER': 
        return 'High threat', score
    elif label == 'FEAR':
        return 'Medium threat', score
    elif label == 'SADNESS':
        return 'Low threat', score
    else:
        return 'Low threat', score
    

def is_threat_near_user(user_coords, threat_coords, threat_text, max_km=10):
    """
    Function to check if the threat is near the user (distance <= max_km) 
    and classify the threat based on the provided text.
    """
    # Calculate the distance between user and threat location
    distance = geodesic(user_coords, threat_coords).km

    # Classify the threat based on the text
    threat_class, confidence = classify_threat(threat_text)

    # Determine if the threat is near the user
    if distance <= max_km:
        return True, threat_class, confidence  # Threat is near, with classification and confidence
    else:
        return False, threat_class, confidence
    

user_coords = (40.7128, -74.0060)  
threat_coords = (40.7306, -73.9352)  
threat_text = "I'm going to destroy everything."  
max_km = 10  

# Call the function
is_near, threat_type, confidence = is_threat_near_user(user_coords, threat_coords, threat_text, max_km)

# Output the result
print(f"Is the threat near? {is_near}")
print(f"Threat classification: {threat_type} (Confidence: {confidence:.2f})")
