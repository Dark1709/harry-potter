from django.db import models

class Spell(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Spell"
        verbose_name_plural = "Spells"
    
    def __str__(self):
        return self.name