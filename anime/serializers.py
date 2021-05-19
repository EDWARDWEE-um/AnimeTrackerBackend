from rest_framework import serializers
from .models import Anime
from django.conf import settings

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ( 'id','title','type','episodes','image_url','url','synopsis','score','author')
        

