from django.db import models

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    facial_keypoints = models.JSONField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        ordering = ['id']
        app_label = 'Rocket_Elevators_Django_API'
        db_table = 'employees'
