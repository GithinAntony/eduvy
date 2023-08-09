from django.db import models
from college_owners.models import colleges
from super_admin.models import *
# Create your models here.
class faculty(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    college = models.ForeignKey(colleges, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=100, default='null', null=False)
    lastname = models.CharField(max_length=100, default='null', null=False)
    email = models.CharField(max_length=255, default='null', null=False)
    password = models.CharField(max_length=500, default='null', null=False)
    phone = models.CharField(max_length=15, default='null', null=False)
    address = models.TextField(default='null', null=False)
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="active")

    def __str__(self):
        return self.firstname

class courses(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    college = models.ForeignKey(colleges, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, default='null', null=False)
    description = models.CharField(max_length=500, default='null', null=False)
    course_type = models.ForeignKey(CourseType, on_delete=models.SET_NULL, null=True)
    course_stream = models.ForeignKey(CourseStream, on_delete=models.SET_NULL, null=True)
    choice_year = [
        ('1', '1 Year'),
        ('2', '2 Year'),
        ('3', '3 Year'),
        ('4', '4 Year'),
        ('5', '5 Year'),
        ('6', '6 Year'),
        ('7', '7 Year'),
        ('8', '8 Year'),
    ]
    duration = models.CharField(max_length=15, choices=choice_year, default="1")

    def __str__(self):
        return self.name





