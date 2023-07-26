from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name