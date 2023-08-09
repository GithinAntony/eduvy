from django.db import models
from college_owners.models import colleges

# Create your models here.
class teacher(models.Model):
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