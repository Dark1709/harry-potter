from colorfield.fields import ColorField
from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default='#FFFFFF')
    animal = models.CharField(max_length=100)
    founder = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"
        
    def __str__(self):
        return self.name