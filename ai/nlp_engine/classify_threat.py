from transformers import pipeline
import torch 

device = torch.device('cpu')

local_model_path = "/Users/tanishrajput/Desktop/SafeSpace/ai/nlp_engine/bhadresh-bert-emotion-model"
classifier = pipeline("text-classification", model=local_model_path, tokenizer=local_model_path)

def detect_threat(text):
    result = classifier(text)[0]
    return result["label"], result["score"]



