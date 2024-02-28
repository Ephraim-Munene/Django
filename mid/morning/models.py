from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Dorm(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
