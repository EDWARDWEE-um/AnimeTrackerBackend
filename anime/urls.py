from .views import AnimeList, CreateAnimePost, DeleteAnimePost
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'anime'

router = DefaultRouter()
router.register('', AnimeList, basename='anime')


urlpatterns = [
    # Post Admin URLs
    path('', include(router.urls)),
    path('create/', CreateAnimePost.as_view(), name='createanime'),
    path('delete/<int:pk>/', DeleteAnimePost.as_view(), name='deleteanime'),
]