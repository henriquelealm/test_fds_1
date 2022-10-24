from django.contrib.auth.models import User
from django.db import models


# login, registration and comment features in my blog
# Create your models here.
class Comment(models.Model):
    data = models.DateTimeField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=350)

    def __str__(self) -> str:
        return self.content
