from django.db import models


# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.fname + " , " + str(self.age)
    