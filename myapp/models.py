from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.html import format_html


GENDER_CHOICE = (
    ('F','Female'),
    ('M','Male'),
)

# Create your models here.
class Person(AbstractUser):
    # fname = models.CharField(max_length=100)
    # lname = models.CharField(max_length=100)
    age = models.IntegerField(null=True)  #เป็นค่าว่างได้
    # username = models.CharField(max_length=20, unique=True)
    # email = models.EmailField(unique=True, null=False, blank=False)
    # password = models.CharField(max_length=20)
    #is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)
    gender = models.CharField(max_length=5 , null=True , blank=True , choices=GENDER_CHOICE)
    image = models.FileField(upload_to = 'upload/' , null=True , blank=True)


    def __str__(self):
        return self.username
    
    def show_image(self):
        if self.image:
            return format_html('<img src="' + self.image.url + '"heigh="40px">')
        return ''
    show_image.allow_tags = True
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name