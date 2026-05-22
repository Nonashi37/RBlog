from django.db.models import Q
from rest_framework import viewsets, generics, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        # Guests only see published posts. Authenticated users see published posts OR their own drafts.
        user = self.request.user
        if user.is_authenticated:
            return Post.objects.filter(Q(is_published=True) | Q(author=user))
        return Post.objects.filter(is_published=True)

    def perform_create(self, serializer):
        # This is where we automatically inject the logged-in user as the author
        serializer.save(author=self.request.user)


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        # Pull the post_id straight out of the URL parameters
        return Comment.objects.filter(post_id=self.kwargs['post_id'], is_approved=True)

    def perform_create(self, serializer):
        # Automatically attach the author AND the parent post to the comment
        serializer.save(author=self.request.user, post_id=self.kwargs['post_id'])