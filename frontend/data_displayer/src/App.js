import './App.css';
import { useState } from 'react';

function App() {
  const [loading, setLoading] = useState(false);
  const API_URL = 'http://localhost:8000/api'; // Replace with your actual API endpoint

  // Function to handle JSON download
  const handleJsonDownload = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/data`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      const data = await response.json();
      
      // Create a blob and download it
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      
      const a = document.createElement('a');
      a.href = url;
      a.download = 'data.json';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Error downloading JSON:', error);
      alert('Failed to download JSON data');
    } finally {
      setLoading(false);
    }
  };

  // Function to handle XLSX download
  const handleXlsxDownload = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/data/xlsx`, {
        method: 'GET',
        headers: {
          'Accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        }
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      // For binary data like XLSX, we need to use blob()
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      
      const a = document.createElement('a');
      a.href = url;
      a.download = 'data.xlsx';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Error downloading XLSX:', error);
      alert('Failed to download XLSX data');
    } finally {
      setLoading(false);
    }
  };

  // Function to view visualizations
  const handleViewVisualizations = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/data_visualisation`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      const data = await response.json();
      // Here you would typically update state with the visualization data
      // and render it in your component or navigate to a visualization page
      console.log('Visualization data:', data);
      
      // Example: You might want to redirect to a visualization page
      // window.location.href = '/visualizations';
    } catch (error) {
      console.error('Error loading visualizations:', error);
      alert('Failed to load visualizations');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <div>
          Data retrieval app
        </div>
        <div className="button-container">
          <button 
            className="app-button" 
            onClick={handleJsonDownload}
            disabled={loading}
          >
            {loading ? 'Loading...' : 'Download data as json'}
          </button>
          <button 
            className="app-button" 
            onClick={handleXlsxDownload}
            disabled={loading}
          >
            {loading ? 'Loading...' : 'Download data as xlsx'}
          </button>
          <button 
            className="app-button" 
            onClick={handleViewVisualizations}
            disabled={loading}
          >
            {loading ? 'Loading...' : 'View visualisations'}
          </button>
        </div>
      </header>
    </div>
  );
}

export default App;