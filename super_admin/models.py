from django.db import models
# Create your models here.
class superAdmin(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
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
        return self.unique_id

class State(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, default='null', null=False)
    code = models.CharField(max_length=10, default='null', null=False)

    def __str__(self):
        return self.name

class City(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, default='null', null=False)

    def __str__(self):
        return self.name

class CourseType(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, default='null', null=False)
    description = models.CharField(max_length=500, default='null', null=False)

    def __str__(self):
        return self.name

class CourseStream(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, default='null', null=False)
    description = models.CharField(max_length=500, default='null', null=False)

    def __str__(self):
        return self.name
