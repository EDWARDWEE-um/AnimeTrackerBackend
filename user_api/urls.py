from .views import PostList ,CreatePost, EditPost, AdminPostDetail,  DeletePost
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'user_api'

router = DefaultRouter()
router.register(r'a', PostList, basename='post')


urlpatterns = [
    # Post Admin URLs
    path('', include(router.urls)),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]