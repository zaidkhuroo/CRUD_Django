from django.db import models

# Create your models here.
class Entries(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + " " + self.last_name #with this record in the django admin would be shown as by first name and the last name