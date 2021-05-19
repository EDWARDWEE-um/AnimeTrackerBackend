from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Anime
from .serializers import AnimeSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, BasePermission
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class AnimeList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AnimeSerializer
    authentication_classes = [JWTAuthentication]
   
    def get_queryset(self):
        return Anime.objects.filter(author=self.request.user.email)

    
# Post Admin

class CreateAnimePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = AnimeSerializer
    def get_queryset(self):
        return Anime.objects.filter(author=self.request.user)


class DeleteAnimePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = AnimeSerializer
    def get_queryset(self):
        return Anime.objects.filter(author=self.request.user)