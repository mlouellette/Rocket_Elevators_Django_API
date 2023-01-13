# Rocket_Elevators_Django_API

This application uses Python's DJANGO framework and REST API to make requests. It's using the facial recognition open source library to allow for registering employees to a database or searching for an employee by using a picture. If the employee is found in the database's employee's table, their credentials will be returned.

## Usage

`python manage.py runserver`

## Url samples 

You can test different scenario's on the interface of your choice
I recommend using POSTMAN : https://www.postman.com/downloads/

- POST : http://127.0.0.1:8000/employees
- GET : http://127.0.0.1:8000/employees
- GET : http://127.0.0.1:8000/employees/recognize
- GET : http://127.0.0.1:8000/employees/1

## Facial Recognition library 

- https://github.com/ageitgey/face_recognition

## Presentation video

- https://vimeo.com/789114480
