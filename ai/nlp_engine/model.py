from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Specify the model name on Hugging Face Model Hub
model_name = "bhadresh-savani/bert-base-uncased-emotion"
local_model_path = "bhadresh-bert-emotion-model"  # Directory to save model files

# Download the model and tokenizer from Hugging Face
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save model and tokenizer locally
model.save_pretrained(local_model_path)
tokenizer.save_pretrained(local_model_path)