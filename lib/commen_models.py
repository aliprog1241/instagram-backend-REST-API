from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    created_time = models.DateTimeField(_("created time"), auto_now_add=True)
    modified_time = models.DateTimeField(_("modify time"), auto_now_add=True)

    class Meta:
        abstract = True