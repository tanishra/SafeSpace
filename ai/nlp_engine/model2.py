from transformers import pipeline, BertForTokenClassification, BertTokenizer

# Download and save the model and tokenizer
model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"

# Load model and tokenizer from Hugging Face
model = BertForTokenClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Save model and tokenizer locally
model.save_pretrained("./bert-large-ner")
tokenizer.save_pretrained("./bert-large-ner")

