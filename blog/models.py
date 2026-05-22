from django.conf import settings
from django.db import models


class Post(models.Model):
    """
    Represents a blog article written by a user.
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        # Indexes speed up lookups if you query by published state frequently
        indexes = [
            models.Index(fields=["is_published", "-created_at"]),
        ]

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    Represents a comment left by a user on a specific blog post.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    body = models.TextField()
    is_approved = models.BooleanField(default=True)     # True means visible immediately
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Comment by {self.author.username} on '{self.post.title}'"