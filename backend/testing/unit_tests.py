import pytest
import pandas as pd
import json
import os
from test_unified_data_structure import Unified_data_structure

@pytest.fixture
def uds():
    return Unified_data_structure()

def test_init(uds):
    assert isinstance(uds.data, dict)
    assert len(uds.data) > 0

def test_read_json(uds):
    assert "companies" in uds.data
    assert "employees" in uds.data
    assert "companies_performance" in uds.data
    assert isinstance(uds.data["companies"], pd.DataFrame)
    assert isinstance(uds.data["employees"], dict)
    assert isinstance(uds.data["companies_performance"], pd.DataFrame)

def test_read_csv(uds):
    assert "customers" in uds.data
    assert isinstance(uds.data["customers"], pd.DataFrame)

def test_read_pdf(uds):
    assert "quarterly_performance" in uds.data
    assert isinstance(uds.data["quarterly_performance"], pd.DataFrame)

def test_read_pptx(uds):
    assert "revenue_distribution" in uds.data
    assert "key_highlights" in uds.data
    assert "quarterly_metrics" in uds.data
    assert isinstance(uds.data["quarterly_metrics"], pd.DataFrame)

def test_get_data(uds, tmp_path):
    uds.get_data()
    json_file = 'datasets/consolidated_dataset.json'
    assert os.path.exists(json_file)
    with open(json_file, 'r') as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert "employees" in data

def test_get_data_xlsx(uds):
    uds.get_data_xlsx()
    xlsx_file = 'datasets/consolidated_dataset.xlsx'
    assert os.path.exists(xlsx_file)

def test_visualise_data(uds):
    uds.visualise_data()
    png_file = 'datasets/data_visualisations.png'
    assert os.path.exists(png_file)
