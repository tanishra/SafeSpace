from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Model name
model_name = "j-hartmann/emotion-english-distilroberta-base"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Save the model and tokenizer locally
save_path = "threat_model"  
tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)
