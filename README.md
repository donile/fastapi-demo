# FastAPI Demo

## Start API
`> uvicorn app.main:app --reload`

## Installing Python3.9
`> sudo apt update`
`> sudo apt install software-properties-common`
`> add-apt-repository ppa:deadsnakes/ppa`
`> sudo apt update`
`> sudo apt install python3.9 python3.9-venv python3.9-dev`
`> python3.9 -m pip install virtualenv`
`> python3.9 -m virtualenv venv`

## TODO
Authentication  
* Add salt to password hashing
* Inject password hashing salt from environment variable
* Rename models.password_verifier module

Database ORM  
Database migrations  
Many-to-many mappings  

## Notes
`FastAPI` is a class that inherits from `Starlette`  
