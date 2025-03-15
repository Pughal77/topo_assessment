from fastapi import FastAPI, HTTPException, Path
from typing import Dict, Any
from fastapi.responses import FileResponse
from unified_data_structure import Unified_data_structure
import json


class DataAPIServer:
    """
    A class-based FastAPI server implementation that provides data endpoints.
    """
    
    def __init__(self):
        """Initialize the FastAPI application with configuration and routes."""
        self.app = FastAPI(
            title="Data API",
            description="A class-based API with two endpoints for retrieving data",
            version="1.0.0"
        )
        self._configure_routes()
        ''' Iniitialise unified data structure'''
        self.unified_data_structure = Unified_data_structure()
    
    def _configure_routes(self):
        """Configure the API routes and endpoints."""
        self.app.add_api_route(
            path="/api/data",
            endpoint=self.get_data,
            methods=["GET"],
            response_model=Any, # specify type of response object later
            summary="Get all data",
            description="Retrieve all data without any parameters."
        )
        
        self.app.add_api_route(
            path="/api/data/{file_type}",
            endpoint=self.get_data_by_type,
            methods=["GET"],
            response_model=Any, # specify type of response object later
            summary="Get data by file type",
            description="Retrieve data based on the specified file type."
        )
    
    async def get_data(self):
        """
        Retrieve all data without any parameters.
        
        Returns:
        """
        # This function is intentionally left empty for now
        return  self.unified_data_structure.get_data()
    
    async def get_data_by_type(self, file_type: str):
        """
        Retrieve data based on the specified file type.
        
        Args:
            file_type (str): The type of file to retrieve. For now it supports only
            csv and json
            
        Returns: a xlsx file or json object
        """

        if file_type == "xlsx":
            self.unified_data_structure.get_data_xlsx()
            file_path = "datasets/consolidated_dataset.xlsx"
            return FileResponse(
                path=file_path,
                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                filename="consolidated_dataset.xlsx"  # Suggested filename for download
            )
        elif file_type == "json":
            return self.unified_data_structure.get_data()

    
    def run(self, host: str = "0.0.0.0", port: int = 8000):
        """
        Run the FastAPI application.
        
        Args:
            host (str): The host to bind to
            port (int): The port to bind to
        """
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)


# Create an instance of the server
api_server = DataAPIServer()

# Get the FastAPI application instance
app = api_server.app

if __name__ == "__main__":
    # Run the server if this file is executed directly
    api_server.run()