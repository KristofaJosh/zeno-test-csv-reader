# zeno-test-csv-reader

an application that reads a csv file and transfers it to a database (SQL)

# Usage
- Online [Zeno CSV-DB](https://zenocsvtodb.netlify.app/) app

- Docker [image]()
    - to run in docker container, run:
        - docker compose build
        - **docker-compose up** 
        - then wait for both services to start.
        you should have servers on ports 
        _localhost:3000_ and _localhost:8000_ running
    
- local 
    - navigate into **./backend/zeno_server/** 
        - run _python manage.py runserver_
    - navigate into **./frontend**
        - run _yarn start_

# Docs
- view the documentation of this project in **./docs** folder

### Tools used for this project
- Python (Django)
- JavaScript (React)


### Possible errors
Could Not Shared Drives in Docker Settings. Firewall detected Error.
- goto [Shared Drive](https://github.com/docker/for-win/issues/5456)