# data/data_loader.py

import os
import json
from typing import List, Dict, Any

class DataLoader:
    """
    Class to load and preprocess data for the DAG-based reasoning framework.
    Handles JSON files containing reasoning data for LLMs.
    """

    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def load_data(self) -> List[Dict[str, Any]]:
        """Load JSON data from the specified directory."""
        data = []
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.data_dir, filename), "r") as file:
                    data.append(json.load(file))
        return data

    def preprocess(self, raw_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Basic preprocessing to ensure data consistency (e.g., token conversion)."""
        return [{"text": d.get("text", "").strip(), "label": d.get("label")} for d in raw_data]
