## Overview: A description of your solution and approach.
Approach is to use python modules for data visualisation and use FastApi to set up our API endpoints
Simple frontend using react to provide simple user experience to get files and visualisations




## Setup Instructions: Steps to run the app locally and access the API.
Install required dependencies:
```
pip install -r requirements.txt
```
1. cd into the backend directory,
First run the python server
```
cd backend
python server.py
```
2. cd into the data_displayer directory, to start the react application,
```
cd frontend/data_displayer
npm run start
```


## Testing Instructions: Steps to execute unit and integration tests.
cd into the testing directory and run pytests
```
cd testing
pytest
```

## Assumptions or Challenges: Any assumptions or challenges you faced


 - Assumptions - this application works only in the context of these 4 datasets

 - Challenges -
    * It took some time to come to terms with how the unified data structure should be structured but due to a lack of time, I decided to settle with a simple one (I considered using a nosql database to store all 4 datasets but it was tough coming up with an appropriate schema)

    * Coming up with visualistations of the data. I had a hard time deciding of cmoing up with meaningful visualisations

    * I am not sure what to do with null values in the context of this dataset. I am not sure if I am to replace null values with
    appropriate values (like 0) or just remove them (resulting in a loss of significant data)

    * Fixing bugs of converting pandas dataframe to JSON
## Future Improvements
 - Improve sturcture of unified dataset
 - Improve test coverage for application (unit tests for `unified_data_structue` only include postive test cases for now).
 - Unit tests for the frontend application and for the API needs to be able to 