from django.db import models

# Create your models here.

class credential(models.Model):
    name = models.CharField(max_length=50)
    pno = models.CharField(max_length=14)
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profile = models.ImageField()
    
    def __str__(self):
        return self.name
    