from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','firstName' ,'lastName','title', 'email', 'password', 'facial_keypoints', 'created_at', 'updated_at']