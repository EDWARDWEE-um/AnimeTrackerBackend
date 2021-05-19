from django.urls import path, include
from .views import CustomUserCreate, BlacklistTokenUpdateView, UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'users'
router = DefaultRouter()
router.register('', UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls)),
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]