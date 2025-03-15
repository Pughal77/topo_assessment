import os
import pytest
import pandas as pd
import numpy as np
import json
from unittest.mock import patch, MagicMock, mock_open
from io import StringIO

# Import the class to test
# Assuming the class is in a file called data_unifier.py
from test_unified_data_structure import Unified_data_structure

class TestUnifiedDataStructure:
    
    @pytest.fixture
    def mock_datasets(self):
        """Fixture to create mock datasets for testing"""
        # Mock JSON data
        mock_json = {
            "companies": [
                {
                    "name": "Sports and Leisure",
                    "industry": "Fitness",
                    "employees": [
                        {"id": 1, "name": "John Doe", "position": "Manager"},
                        {"id": 2, "name": "Jane Smith", "position": "Trainer"}
                    ],
                    "performance": {"revenue": 500000, "growth": "5%"}
                }
            ]
        }
        
        # Mock CSV data
        mock_csv = pd.DataFrame({
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
            "membership": ["Premium", "Basic", "Premium"],
            "Location": ["Downtown", "Suburban", "Downtown"]
        })
        
        # Mock PDF data
        mock_pdf = pd.DataFrame({
            "Quarter": ["Q1", "Q2", "Q3", "Q4"],
            "Revenue (in $)": [2500000, 2700000, 3000000, 2200000]
        })
        
        # Mock PPTX data
        mock_quarterly_metrics = pd.DataFrame({
            "Metric": ["New Members", "Renewals", "Cancellations"],
            "Q1": ["450", "300", "120"],
            "Q2": ["480", "350", "100"]
        })
        
        mock_key_highlights = {
            "Total Revenue": "$10,400,000",
            "Total Memberships Sold": "1520",
            "Top Location": "Downtown"
        }
        
        mock_revenue_distribution = {
            "Gym": "40%",
            "Pool": "25%,",
            "Tennis Court": "15%",
            "Personal Training": "20%"
        }
        
        return {
            "mock_json": mock_json,
            "mock_csv": mock_csv,
            "mock_pdf": mock_pdf,
            "mock_quarterly_metrics": mock_quarterly_metrics,
            "mock_key_highlights": mock_key_highlights,
            "mock_revenue_distribution": mock_revenue_distribution
        }
    
    @pytest.fixture
    def setup_mocks(self, mock_datasets, monkeypatch):
        """Set up mocks for all external dependencies"""
        # Mock pandas read_json
        def mock_read_json(*args, **kwargs):
            return pd.DataFrame(mock_datasets["mock_json"])
        
        # Mock pandas read_csv
        def mock_read_csv(*args, **kwargs):
            return mock_datasets["mock_csv"]
        
        # Mock tabula.read_pdf
        def mock_tabula_read_pdf(*args, **kwargs):
            return [mock_datasets["mock_pdf"]]
        
        # Mock Presentation for PPTX
        mock_presentation = MagicMock()
        mock_slide = MagicMock()
        mock_shape = MagicMock()
        mock_table = MagicMock()
        
        # Create mock rows and cells
        mock_cell1 = MagicMock()
        mock_cell1.text = "Metric"
        mock_cell2 = MagicMock()
        mock_cell2.text = "Q1"
        mock_cell3 = MagicMock()
        mock_cell3.text = "Q2"
        
        mock_cell4 = MagicMock()
        mock_cell4.text = "New Members"
        mock_cell5 = MagicMock()
        mock_cell5.text = "450"
        mock_cell6 = MagicMock()
        mock_cell6.text = "480"
        
        # Create rows
        mock_row1 = MagicMock()
        mock_row1.cells = [mock_cell1, mock_cell2, mock_cell3]
        mock_row2 = MagicMock()
        mock_row2.cells = [mock_cell4, mock_cell5, mock_cell6]
        
        mock_table.rows = [mock_row1, mock_row2]
        mock_shape.table = mock_table
        mock_slide.shapes = [MagicMock(), mock_shape]  # Second shape is the table
        mock_presentation.slides = [MagicMock(), mock_slide]  # Second slide has the table
        
        # Apply patches
        monkeypatch.setattr(pd, "read_json", mock_read_json)
        monkeypatch.setattr(pd, "read_csv", mock_read_csv)
        monkeypatch.setattr("tabula.read_pdf", mock_tabula_read_pdf)
        monkeypatch.setattr("pptx.Presentation", lambda x: mock_presentation)
        
        # Return the mocked dependencies for reference
        return {
            "mock_presentation": mock_presentation
        }
    
    def test_initialization(self, setup_mocks):
        """Test that the class initializes correctly and calls all the read methods"""
        with patch.object(Unified_data_structure, 'read_json') as mock_read_json, \
             patch.object(Unified_data_structure, 'read_csv') as mock_read_csv, \
             patch.object(Unified_data_structure, 'read_pdf') as mock_read_pdf, \
             patch.object(Unified_data_structure, 'read_pptx') as mock_read_pptx:
            
            uds = Unified_data_structure()
            
            # Check that all read methods were called
            mock_read_json.assert_called_once_with("datasets/dataset1.json")
            mock_read_csv.assert_called_once_with("datasets/dataset2.csv")
            mock_read_pdf.assert_called_once_with("datasets/dataset3.pdf")
            mock_read_pptx.assert_called_once_with("datasets/dataset4.pptx")
            
            # Check that data is initialized as a dictionary
            assert isinstance(uds.data, dict)
    
    def test_read_json(self, setup_mocks, mock_datasets):
        """Test the read_json method"""
        uds = Unified_data_structure()
        
        # Mock the read_json method to use our test data
        with patch.object(Unified_data_structure, '__init__', lambda self: None):
            uds = Unified_data_structure()
            uds.data = {}
            uds.read_json("datasets/dataset1.json")
            
            # Check that the companies data was correctly processed
            assert "companies" in uds.data
            assert isinstance(uds.data["companies"], pd.DataFrame)
            
            # Check that the employees data was correctly processed
            assert "employees" in uds.data
            assert isinstance(uds.data["employees"], dict)
            
            # Check that the company performance data was correctly processed
            assert "companies_performance" in uds.data
            assert isinstance(uds.data["companies_performance"], pd.DataFrame)
    
    def test_read_csv(self, setup_mocks, mock_datasets):
        """Test the read_csv method"""
        # Create an instance with mocked initialization
        with patch.object(Unified_data_structure, '__init__', lambda self: None):
            uds = Unified_data_structure()
            uds.data = {}
            uds.read_csv("datasets/dataset2.csv")
            
            # Check that the customers data was correctly processed
            assert "customers" in uds.data
            assert isinstance(uds.data["customers"], pd.DataFrame)
            assert len(uds.data["customers"]) == len(mock_datasets["mock_csv"])
    
    def test_read_pdf(self, setup_mocks, mock_datasets):
        """Test the read_pdf method"""
        # Create an instance with mocked initialization
        with patch.object(Unified_data_structure, '__init__', lambda self: None):
            uds = Unified_data_structure()
            uds.data = {}
            uds.read_pdf("datasets/dataset3.pdf")
            
            # Check that the quarterly performance data was correctly processed
            assert "quarterly_performance" in uds.data
            assert isinstance(uds.data["quarterly_performance"], pd.DataFrame)
            assert len(uds.data["quarterly_performance"]) == len(mock_datasets["mock_pdf"])
    
    def test_read_pptx(self, setup_mocks, mock_datasets):
        """Test the read_pptx method"""
        # Create an instance with mocked initialization
        with patch.object(Unified_data_structure, '__init__', lambda self: None):
            uds = Unified_data_structure()
            uds.data = {}
            uds.read_pptx("datasets/dataset4.pptx")
            
            # Check that all the expected data was extracted from the presentation
            assert "quarterly_metrics" in uds.data
            assert "key_highlights" in uds.data
            assert "revenue_distribution" in uds.data
            
            # Check that the key_highlights has the expected structure
            assert uds.data["key_highlights"]["Total Revenue"] == "$10,400,000"
            assert uds.data["key_highlights"]["Total Memberships Sold"] == "1520"
            assert uds.data["key_highlights"]["Top Location"] == "Downtown"
            
            # Check that the revenue_distribution has the expected structure
            assert uds.data["revenue_distribution"]["Gym"] == "40%"
            assert uds.data["revenue_distribution"]["Pool"] == "25%,"
    
    def test_get_data(self, setup_mocks):
        """Test the get_data method"""
        # Create an instance with mocked data
        with patch.object(Unified_data_structure, '__init__', lambda self: None):
            uds = Unified_data_structure()
            uds.data = {
                "companies": pd.DataFrame({"name": ["Sports and Leisure"]}),
                "employees": {0: pd.DataFrame({"id": [1, 2], "name": ["John", "Jane"]})},
                "quarterly_performance": pd.DataFrame({"Quarter": ["Q1", "Q2"], "Revenue (in $)": [100, 200]})
            }
            
            # Mock json operations
            mock_json_dump = MagicMock()
            mock_json_file = MagicMock()
            
            with patch("json.dump", mock_json_dump), \
                 patch("json.load", return_value={"test": "data"}), \
                 patch("builtins.open", mock_open()):
                
                result = uds.get_data()
                
                # Check that json.dump was called
                assert mock_json_dump.called
                
                # Check the return value
                assert isinstance(result, dict)
    
    def test_get_data_xlsx(self, setup_mocks):
        """Test the get_data_xlsx method"""
        # Create an instance with mocked data
        with patch.object(Unified_data_structure, '__init__', lambda self: None):
            uds = Unified_data_structure()
            uds.data = {
                "companies": pd.DataFrame({"name": ["Sports and Leisure"]}),
                "employees": {0: pd.DataFrame({"id": [1, 2], "name": ["John", "Jane"]})},
                "quarterly_performance": pd.DataFrame({"Quarter": ["Q1", "Q2"], "Revenue (in $)": [100, 200]}),
                "key_highlights": {"Total Revenue": "$10,400,000"}
            }
            
            # Mock the ExcelWriter
            mock_excel_writer = MagicMock()
            
            with patch("pandas.ExcelWriter", return_value=mock_excel_writer):
                uds.get_data_xlsx()
                
                # Check that to_excel was called for each expected sheet
                # This is a simplified check, we could make it more robust
                assert mock_excel_writer.__enter__.called
    
    def test_get_data_keys(self, setup_mocks):
        """Test the get_data_keys method"""
        # Create an instance with mocked data
        with patch.object(Unified_data_structure, '__init__', lambda self: None):
            uds = Unified_data_structure()
            uds.data = {
                "key1": "value1",
                "key2": "value2"
            }
            
            keys = uds.get_data_keys()
            
            # Check that the keys match
            assert set(keys) == {"key1", "key2"}
    
    def test_visualise_data(self, setup_mocks):
        """Test the visualise_data method"""
        # Create an instance with mocked data
        with patch.object(Unified_data_structure, '__init__', lambda self: None):
            uds = Unified_data_structure()
            uds.data = {
                "customers": pd.DataFrame({
                    "Location": ["Downtown", "Suburban", "Downtown", "Downtown"]
                }),
                "quarterly_performance": pd.DataFrame({
                    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
                    "Revenue (in $)": [100, 200, 300, 400]
                })
            }
            
            # Mock matplotlib functions to avoid actual plotting
            with patch("matplotlib.pyplot.show", MagicMock()), \
                 patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), [MagicMock(), MagicMock()])):
                
                uds.visualise_data()
                # Not much to assert here since we're mocking the plotting functions
                # The test passes if no exceptions are raised