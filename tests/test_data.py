import pytest
import pandas as pd
from pathlib import Path
from src.utils import load_enriched_dataset, calculate_projected_metric, ForecastConfig

def test_dataset_existence():
    """Test if processed dataset exists."""
    path = Path("data/processed/ethiopia_fi_enriched_data.csv")
    alt_path = Path("../data/processed/ethiopia_fi_enriched_data.csv")
    assert path.exists() or alt_path.exists(), "Processed enriched dataset is missing."

def test_load_enriched_dataset():
    """Test that data loader returns a valid pandas DataFrame."""
    try:
        df = load_enriched_dataset()
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
    except FileNotFoundError:
        pytest.skip("Dataset file not found in local environment path.")

def test_schema_columns():
    """Test that mandatory schema headers exist."""
    try:
        df = load_enriched_dataset()
        required = ["record_type", "indicator_code", "observation_date"]
        for col in required:
            assert col in df.columns, f"Missing required column: {col}"
    except FileNotFoundError:
        pytest.skip("Dataset file not found.")

def test_forecast_calculation():
    """Test compound growth projection utility function."""
    val = calculate_projected_metric(49.0, 0.05, 1)
    assert val == 51.45

def test_forecast_config_dataclass():
    """Test configuration dataclass defaults."""
    cfg = ForecastConfig()
    assert cfg.start_year == 2021
    assert cfg.end_year == 2027