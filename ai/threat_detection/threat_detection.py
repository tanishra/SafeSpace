from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Local path to model
local_path = "/Users/tanishrajput/Desktop/SafeSpace/ai/threat_detection/threat_model"

# Load locally saved model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(local_path)
model = AutoModelForSequenceClassification.from_pretrained(local_path)

# Create pipeline using local model
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def get_threat_level(label: str, score_percent: float) -> str:
    """
    Determines the threat level based on the model's label and confidence score.

    Args:
        label (str): The predicted emotion or category (e.g., 'ANGER', 'JOY', 'FEAR').
        score_percent (float): The confidence score as a percentage (e.g., 87.5).

    Returns:
        str: Threat level - 'High Threat', 'Medium Threat', 'Low Threat', or 'No Threat'.
    """

    label = label.upper().strip()

    # Define threat-related labels
    high_threat_labels = {
    # Violent Behavior
    'VIOLENCE', 'MURDER', 'RAPE', 'ASSAULT', 'FIGHT', 'AGGRESSION', 'ANGER', 'HOMICIDE',
    
    # Criminal Threats
    'TERRORISM', 'KIDNAPPING', 'RIOT', 'ROBBERY', 'LOOTING', 'ARSON',

    # Disasters (Man-made/Natural)
    'FIRE', 'EXPLOSION', 'EARTHQUAKE', 'FLOOD', 'BUILDING_COLLAPSE', 'TSUNAMI', 'TORNADO',
    'HURRICANE', 'LANDSLIDE', 'NUCLEAR_ACCIDENT', 'CHEMICAL_SPILL',

    # Transportation Incidents
    'ACCIDENT', 'CAR_CRASH', 'PLANE_CRASH', 'TRAIN_DERAILMENT', 'BOAT_SINKING',

    # Weapons-related
    'GUNSHOT', 'SHOOTING', 'STABBING', 'WEAPON_THREAT', 'BOMB_THREAT',

    # Social Threats
    'HATE', 'LYNCHING', 'GENOCIDE', 'RACISM', 'EXTREMISM'
    }

    medium_threat_labels = {
    # Emotional States
    'FEAR', 'ANXIETY', 'PANIC', 'PARANOIA', 'TENSION',

    # Suspicious Behavior
    'SUSPICIOUS_ACTIVITY', 'TRESPASSING', 'THREATS', 'HARASSMENT', 'ESCALATION',

    # Environmental Warning Signs
    'SMOKE', 'STRUCTURAL_DAMAGE', 'LEAKAGE', 'OVERFLOW',

    # Social/Group Indicators
    'PROTEST', 'UNREST', 'CROWD_BUILDUP', 'VERBAL_ABUSE'
    }

    low_threat_labels = {
    # Emotional States
    'SADNESS', 'WORRY', 'DISTRESS', 'DESPAIR', 'CONFUSION', 'ISOLATION', 'FRUSTRATION',

    # Environmental Cues
    'ODOR', 'VIBRATION', 'MINOR_DAMAGE', 'STRANGE_NOISES',

    # Social or Health Indicators
    'FATIGUE', 'ILLNESS', 'WITHDRAWAL', 'DEPRESSION', 'CRYING', 'YELLING',

    # Behavioral Cues
    'AGITATION', 'RESTLESSNESS', 'LOSS_OF_CONTROL'
    }


    if label in high_threat_labels:
        if score_percent >= 85:
            return "High Threat"
        elif score_percent >= 70:
            return "Medium Threat"
        else:
            return "Low Threat"

    elif label in medium_threat_labels:
        if score_percent >= 80:
            return "Medium Threat"
        else:
            return "Low Threat"

    elif label in low_threat_labels:
        return "Low Threat"

    else:
        # All other labels are not threats (e.g., JOY, NEUTRAL, LOVE, etc.)
        return "No Threat"


# Function to detect threat and return structured list
def detect_threat(texts):
    results = []
    for text in texts:
        output = classifier(text)[0]  # Get top prediction
        score_percent = round(output["score"] * 100, 2)  # Convert to percentage
        threat_level = get_threat_level(output["label"],score_percent)
        results.append({
            "text": text,
            "label": output["label"],
            "score_percent": f"{score_percent}%",
            "threat_level": threat_level
        })
    return results




