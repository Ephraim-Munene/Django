from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField()
    plate = models.IntegerField()
    image = models.ImageField(upload_to='uploads/images', default="logo.png")

    def __str__(self):
        return self.name
