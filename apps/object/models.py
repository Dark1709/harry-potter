from django.db import models

class Object(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Object"
        verbose_name_plural = "Objects"

    def __str__(self):
        return self.name