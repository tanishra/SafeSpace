from transformers import pipeline, BertForTokenClassification, BertTokenizer

# Load your local fine-tuned BERT NER model
model = BertForTokenClassification.from_pretrained("/Users/tanishrajput/Desktop/SafeSpace/ai/nlp_engine/bert-large-ner")
tokenizer = BertTokenizer.from_pretrained("/Users/tanishrajput/Desktop/SafeSpace/ai/nlp_engine/bert-large-ner")

# Initialize the Hugging Face NER pipeline
hf_ner = pipeline("ner", model=model, tokenizer=tokenizer)

def extract_places(text):
    entities = hf_ner(text)
    # Extract tokens labeled as locations (LOC)
    city_names = [entity['word'] for entity in entities if 'LOC' in entity['entity']]
    return city_names



