# BikeRoute 
This is a simple project to show I am able to work with python/django.

## Goal of the project
>A bikeroute service with following functionality
>- Create a bicyle route
>- Leave a review of a route
>- See a list of all reviews
>- See a list of all routes

## Installation
Clone this git repository:
```
git clone https://github.com/ginberg/django-bikeroute-example.git
```
Create a python virtual environment for python3 and activate it.

Go to the project folder:
```
cd bikeroute
```
Install the requirements:
```
pip install -r requirements.txt
```
Run the migrations:
```
python manage.py migrate
```
Start the server:
```
python manage.py runserver
```
This will start the webserver on http://127.0.0.1:8000/.

## Documentation
The API endpoints are:

| Endpoint   | Description |
|------------|-----------|

An automatic generated interactive API documentation can be found under http://127.0.0.1:8000/docs/ if the server is running.
## Tests
To run the tests:
```
python manage.py test
```

