from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


from content.models import Post
from lib.commen_models import BaseModel


User = get_user_model()

class Comment(BaseModel):
    caption =models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='replies', on_delete=models.CASCADE)