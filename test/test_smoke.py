import pandas as pd
import plotly
import streamlit


def test_imports():
    assert pd is not None
    assert plotly is not None
    assert streamlit is not None


def test_sample_data_exists():
    df = pd.read_csv("data/sample_company.csv")
    assert len(df) > 0
    assert "account" in df.columns
    assert "year" in df.columns
    assert "amount" in df.columns