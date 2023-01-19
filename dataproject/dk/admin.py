from django.contrib import admin

# Register your models here.
from .models import Employee,EmployeeAdmin  
admin.site.register(Employee,EmployeeAdmin)