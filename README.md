# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:

### STEP 2:

### STEP 3:

Write your own steps

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

![OUTPUT](./in.png)




## RESULT

program Executed Successfully
