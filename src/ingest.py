"""
ingest.py

Handles loading and basic cleaning of the sales dataset.

Expected usage:
- Load CSV data from the 'data/' folder
- Perform date parsing, type conversions, and missing value handling

This module should return a cleaned DataFrame for downstream use.
"""

class DataIngestor:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_and_clean(self):
        """
        Load the CSV and perform basic cleaning (date parsing, null handling, etc.)
        Returns: pd.DataFrame
        """
        pass  # TODO: implement data loading and minimal preprocessing
