from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


from content.models import Post
from lib.commen_models import BaseModel


User = get_user_model()

class Comment(BaseModel):
    caption =models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.caption


class Like(BaseModel):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')

    def __str__(self):
        return "{} >> {}".format(self.user, self.post)

