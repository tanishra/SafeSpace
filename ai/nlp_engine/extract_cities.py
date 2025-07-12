import logging
from typing import List
from transformers import pipeline, BertForTokenClassification, BertTokenizer

# Configure logging once at module load
logger = logging.getLogger("PlaceExtractor")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Fixed path to your local fine-tuned model directory
MODEL_PATH = "/Users/tanishrajput/Desktop/SafeSpace/ai/nlp_engine/bert-large-ner"

# Global variable to hold the pipeline instance
_ner_pipeline = None


def load_ner_pipeline(model_path: str = MODEL_PATH) -> pipeline:
    """
    Load and initialize the Hugging Face NER pipeline with a fine-tuned BERT model.

    Args:
        model_path (str): Path to the directory containing the fine-tuned model and tokenizer.

    Returns:
        transformers.pipeline: NER pipeline with aggregation enabled.

    Raises:
        RuntimeError: If loading the model or tokenizer fails.
    """
    global _ner_pipeline
    if _ner_pipeline is not None:
        return _ner_pipeline  # It will return the already loaded pipeline

    try:
        logger.info(f"Loading model and tokenizer from: {model_path}")
        model = BertForTokenClassification.from_pretrained(model_path)
        tokenizer = BertTokenizer.from_pretrained(model_path)
        _ner_pipeline = pipeline(
            "ner",
            model=model,
            tokenizer=tokenizer,
            aggregation_strategy="simple"  # Group tokens into entities
        )
        logger.info("NER pipeline loaded successfully.")
        return _ner_pipeline
    except Exception as e:
        logger.error(f"Failed to load model or tokenizer: {e}")
        raise RuntimeError(f"Failed to load model or tokenizer: {e}") from e


def extract_places(text: str) -> List[str]:
    """
    Extract place names (locations) from input text using the fine-tuned BERT NER pipeline.

    Args:
        text (str): Input text to process.

    Returns:
        List[str]: List of extracted place names (may be empty if none found).

    Raises:
        RuntimeError: If the NER pipeline is not loaded or an error occurs during extraction.
    """
    if not text or not text.strip():
        logger.warning("Empty input text received.")
        return []

    try:
        ner_pipeline = load_ner_pipeline()
        entities = ner_pipeline(text)
        places = [entity['word'] for entity in entities if entity.get('entity_group') == 'LOC']
        logger.info(f"Extracted {len(places)} place(s) from text.")
        return places
    except Exception as e:
        logger.error(f"Error extracting places: {e}")
        raise RuntimeError(f"Error extracting places: {e}") from e

