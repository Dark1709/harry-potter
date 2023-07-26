from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
    
    def __str__(self):
        return self.name