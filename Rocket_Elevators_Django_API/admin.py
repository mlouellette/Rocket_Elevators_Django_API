from django.contrib import admin
from .models import Employee
from django.utils.html import mark_safe

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'password', 'facial_keypoints']

    def facial_keypoints(self, obj):
        return mark_safe(f'<img src="/media/{obj.image}" width="100" height="100" \>')

