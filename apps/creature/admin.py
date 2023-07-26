from django.contrib import admin
from .models import Creature

# Register your models here.
@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'description']
