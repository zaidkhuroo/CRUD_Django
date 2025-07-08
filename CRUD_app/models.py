from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True) 
    password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)
    full_name=models.CharField(max_length=200)

    REQUIRED_FIELDS = ['password', 'confirm_password']  # Required fields for the user model
    USERNAME_FIELD = 'username'  # The field to use as the unique identifier for authentication
class Entries(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Establishing a foreign key relationship with CustomUser
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=20, default='New')  # Default status is 'new'
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date
    date = models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + " " + self.last_name #with this record in the django admin would be shown as by first name and the last name