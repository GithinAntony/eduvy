from django.db import models
from super_admin.models import *
# Create your models here.
class collegeOwner(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    firstname = models.CharField(max_length=100, default='null', null=False)
    lastname = models.CharField(max_length=100, default='null', null=False)
    email = models.CharField(max_length=255, default='null', null=False)
    password = models.CharField(max_length=500, default='null', null=False)
    phone = models.CharField(max_length=15, default='null', null=False)
    address = models.TextField(default='null', null=False)
    profile_photo = models.FileField(upload_to='documents/')
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="active")

    def __str__(self):
        return self.unique_id

class colleges(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    owner = models.ForeignKey(collegeOwner, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, default='null', null=False)
    phone = models.CharField(max_length=15, default='null', null=False)
    website = models.CharField(max_length=200, default='null', null=False)
    email = models.CharField(max_length=200, default='null', null=False)
    address = models.TextField(default='null', null=False)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="active")

    def __str__(self):
        return self.name








