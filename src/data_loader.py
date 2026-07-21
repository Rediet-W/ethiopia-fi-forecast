import pandas as pd
from pathlib import Path

def load_unified_data(filepath="data/raw/ethiopia_fi_unified_data.csv"):
    path = Path(filepath)
    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    df = pd.read_csv(path)
    return df

def validate_schema(df):
    required_columns = [
        "record_type", "pillar", "indicator_code", "value_numeric", 
        "observation_date", "source_name", "source_url", "confidence"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing mandatory schema column: {col}")
    return True