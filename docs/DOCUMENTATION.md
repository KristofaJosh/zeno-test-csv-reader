This is a **Minimal Viable Product** that illustrates extracting data from the provided CSV file and sending it to a database, 
after which, this data is presented to the user in a web app.

##### For this project assumptions are:
- No data will be deleted 
- Data will and can only be added or data can be updated if it exists
- CSV has a defined format [id, temperature, duration, timestamp] any other format will not work.

##### Choice of Database
- for this project, I chose to use **sqlite3** for it's portability and serverless operations.

##### Application
- I speculated between using _pandas_ module or the inbuilt _csv_ module python provides. I decided to use the pandas module
because, pandas was built to manipulate data like this and it is more perfomant than the latter, also describing data like this is much clearer with it and it requires less code.
- Logging the GET request, I didn't understand the question entirely ( On each GET request, log that the data was requested)
    my guesses were:
    - to allow the user call the rows individually
    - log the request on each load of the web app
    
##### Methods Used for API
- GET 
- PATCH 

_PATCH method is used to make changes to part of the data_
_PUT method was not used because it only allows a complete replacement of a document._

### Docker

