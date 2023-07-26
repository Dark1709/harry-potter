from django.contrib import admin
from .models import Spell

# Register your models here.
@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']