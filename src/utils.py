from dataclasses import dataclass
from typing import Optional, List
import pandas as pd
from pathlib import Path

@dataclass
class ForecastConfig:
    start_year: int = 2021
    end_year: int = 2027
    baseline_growth_rate: float = 0.045
    optimistic_boost: float = 0.02
    pessimistic_drag: float = -0.02

def load_enriched_dataset(filepath: str = "data/processed/ethiopia_fi_enriched_data.csv") -> pd.DataFrame:
    """Safely loads the enriched unified dataset with path fallback resolution."""
    paths = [Path(filepath), Path(f"../{filepath}"), Path(f"../../{filepath}")]
    for p in paths:
        if p.exists():
            return pd.read_csv(p)
    raise FileNotFoundError(f"Enriched dataset could not be found at {filepath}")

def calculate_projected_metric(base_val: float, growth_rate: float, years_ahead: int) -> float:
    """Utility function applying compound growth projections."""
    return round(base_val * ((1 + growth_rate) ** years_ahead), 2)