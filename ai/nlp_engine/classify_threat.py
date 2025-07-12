from transformers import pipeline
import torch 

device = torch.device('cpu')

local_model_path = "/Users/tanishrajput/Desktop/SafeSpace/ai/nlp_engine/bhadresh-bert-emotion-model"
classifier = pipeline("text-classification", model=local_model_path, tokenizer=local_model_path)

def detect_threat(text):

    if not isinstance(text, str):
        raise ValueError(f"Expected a string, but got {type(text)}")
    

    if not text.strip():
        raise ValueError("Input text is empty or only whitespace")
    
    # result = classifier(text)[0]
    # return result["label"], result["score"]
    try:
        result = classifier([text])  
        print(f"Classifier output: {result}")  
        return result[0]
    except Exception as e:
        print(f"Error during classification: {e}")
        raise



