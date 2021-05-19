from django.contrib import admin

# Register your models here.
from . import models



class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'title','type','episodes','image_url','url','synopsis','score','published')


admin.site.register(models.Anime)

