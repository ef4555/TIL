from django.contrib import admin
from .models import Article


# Register your models here.
# admin.site.register(Article)
class ArtivcleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')