# models/model_loader.py

from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Tuple

class ModelLoader:
    """
    Class to load and configure the pre-trained language model.
    Adds role-specific tokens for DAG reasoning (e.g., proposer, critic).
    """

    def __init__(self, model_name: str = "gpt2"):
        self.model_name = model_name
        self.model, self.tokenizer = self.load_model_and_tokenizer()

    def load_model_and_tokenizer(self) -> Tuple[AutoModelForCausalLM, AutoTokenizer]:
        """Loads the pre-trained model and tokenizer."""
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForCausalLM.from_pretrained(self.model_name)
        return model, tokenizer

    def add_special_tokens(self, special_tokens: dict):
        """Adds custom tokens to the tokenizer and resizes the model embeddings."""
        self.tokenizer.add_special_tokens(special_tokens)
        self.model.resize_token_embeddings(len(self.tokenizer))

    def get_model_and_tokenizer(self) -> Tuple[AutoModelForCausalLM, AutoTokenizer]:
        """Returns the model and tokenizer for external use."""
        return self.model, self.tokenizer
