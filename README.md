# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![OUTPUT](./in.png)





### STEP 1:

clone the problem to github


### STEP 2:


Createa newapp


### STEP 3:

Enter the code for Admin.py and Model.py

### STEP 4;


Execute Django admin and create 10 employees

## PROGRAM

```
Model.py

from django.db import models
from django.contrib import admin
class Employee (models.Model):
    eid=models.CharField(max_length=20,help_text="Employee ID")
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid','name','salary','age','email')


admin.py

from django.contrib import admin
from .models import Employee,EmployeeAdminadmin
admin.site.register(Employee,EmployeeAdmin)


```

## OUTPUT
![OUTPUT](./Out.png)

## RESULT
program Executed Successfully
