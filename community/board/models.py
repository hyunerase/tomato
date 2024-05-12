from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default = '')
    body = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
   post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE, related_name="comments")
   comment = models.TextField(default='')
   created_at = models.DateTimeField(auto_now_add=True)