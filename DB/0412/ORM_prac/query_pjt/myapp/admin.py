from django.contrib import admin
from .models import PetSitter, Pet

# Register your models here.
admin.site.register(Pet)
admin.site.register(PetSitter)
