from django.contrib import admin
from .models import Character

# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'subspecies', 'gender', 'house', 'school', 'birthdate', 'deathdate', 'bio']

