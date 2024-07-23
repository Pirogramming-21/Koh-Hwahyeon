from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=30)
    profile_photo = models.ImageField(upload_to='profile_photo/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'