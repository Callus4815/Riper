from django.contrib import admin

# Register your models here.
from .models import Fruit


class FruitAdmin(admin.ModelAdmin):
	list_display = ['name', 'color', 'type', 'description']



admin.site.register(Fruit, FruitAdmin)