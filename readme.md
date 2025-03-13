Overview: A description of your solution and approach.
Approach is to use python modules for data visualisation and use FastApi to set up our API endpoints





Setup Instructions: Steps to run the app locally and access the API.



Testing Instructions: Steps to execute unit and integration tests.


Assumptions or Challenges: Any assumptions or challenges you faced

Assumptions - this application works only in the context of these 4 datasets

Challenges -
    It took some time to come to terms with how the unified data structure should be structured but due to a lack of time, I decided to settle with a simple one (I considered using a nosql database to store all 4 datasets but it was tough coming up with an appropriate schema)

    Coming up with visualistations of the data. I had a hard time deciding of cmoing up with meaningful visualisations

    I am not sure what to do with null values in the context of this dataset. I am not sure if I am to replace null values with
    appropriate values (like 0) or just remove them (resulting in a loss of significant data)


Future Improvements
    Improve sturcture of unified dataset