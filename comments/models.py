from django.db import models


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField(unique=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
#    parent_comment = ?