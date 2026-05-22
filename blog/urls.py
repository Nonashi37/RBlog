from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentListCreateView

# The router automatically spins up standard REST endpoints for the ViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    path('', include(router.urls)),
]