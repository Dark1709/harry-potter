from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    subspecies = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    birthdate = models.DateField()
    deathdate = models.DateField(null=True, blank=True)
    bio = models.TextField()
    
    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        return self.name