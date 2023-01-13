from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import face_recognition
import json
import numpy as np
from PIL import Image
from datetime import datetime

# GET/POST, /employees
# Get the data of all employees, Posts to register a new employee
@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        
        # Encoding pictures to json
        image = face_recognition.load_image_file(request.data['img'])
        unknown_face_encoding = face_recognition.face_encodings(image)[0]
        pictureJson = json.loads(json.dumps(list(unknown_face_encoding)))
        data = {
            'firstName': request.data['firstName'],
            'lastName': request.data['lastName'],
            'title': request.data['title'],
            'email': request.data['email'],
            'password': request.data['password'],
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'facial_keypoints': pictureJson
        }
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Facial recognition to return data of an employee if there's a photo match, else return not found
#GET, employees/recognize
@api_view(['GET'])
def recognize_employee(request):
    if request.method == 'GET':
        image = Image.open(request.data['img'])
        img_arr = np.array(image)
        unknown_face_encoding = face_recognition.face_encodings(img_arr)[0]
        employee = Employee.objects.filter(facial_keypoints=unknown_face_encoding.tolist()).first()
        if employee:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        else:
            return Response("Employee not found.")

# GET/DELETE, employees/{id} returns data for a specified id
@api_view(['GET', 'DELETE'])
def employee_detail(request, id):

    try:
        employees = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data)
 
    elif request.method == 'DELETE':
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



