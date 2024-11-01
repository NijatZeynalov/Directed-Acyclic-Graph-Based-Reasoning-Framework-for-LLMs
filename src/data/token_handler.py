# data/token_handler.py

from typing import List

class TokenHandler:
    """
    Handles the insertion and management of role-specific tokens
    (e.g., <proposer>, <critic>, <summarizer>) for reasoning roles.
    """

    SPECIAL_TOKENS = {
        "proposer": "<proposer>",
        "critic": "<critic>",
        "summarizer": "<summarizer>"
    }

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.add_special_tokens()

    def add_special_tokens(self):
        """Adds special tokens to the tokenizer if they are not already present."""
        self.tokenizer.add_tokens(list(self.SPECIAL_TOKENS.values()))

    def tokenize_with_roles(self, text: str, role: str) -> List[int]:
        """Tokenizes text with a specified role token."""
        role_token = self.SPECIAL_TOKENS.get(role, "")
        return self.tokenizer.encode(f"{role_token} {text}", add_special_tokens=True)
