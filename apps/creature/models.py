from django.db import models

class Creature(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Creature"
        verbose_name_plural = "Creatures"

    def __str__(self):
        return self.name