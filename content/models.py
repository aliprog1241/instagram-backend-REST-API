from django.contrib.auth import get_user_model
from django.db import models
from lib.commen_models import BaseModel
from django.utils.translation import gettext_lazy as _
from location.models import Location
from django.core.validators import FileExtensionValidator

User = get_user_model()


class Post(BaseModel):
    caption = models.TextField(_("caption"), blank=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, related_name="posts", on_delete=models.CASCADE, blank=True
    )

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return "{} ({})".format(self.user, self.id)


class PostMedia(BaseModel):
    IMAGE = 1
    VIDEO = 2

    TYPE_CHOICES = (
        (IMAGE, _("Image")),
        (VIDEO, _("Video")),
    )
    media_type = models.PositiveSmallIntegerField(
        _("media_type"), choices=TYPE_CHOICES, default=IMAGE
    )
    post = models.ForeignKey(Post, related_name="media", on_delete=models.CASCADE)
    media_file = models.FileField(
        _("media_file"),
        upload_to="content/media/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=("jpg", "jpeg", "mp4", "wmv", "flv", "png")
            )
        ],
    )

    class Meta:
        verbose_name = _("PostMedia")
        verbose_name_plural = _("PostMedia")

    def __str__(self):
        return "{} - {}".format(str(self.post), self.get_media_type_display())


class Tag(BaseModel):
    title = models.CharField(_("title"), max_length=32)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title


class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name="hashtags", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("PostTag")
        verbose_name_plural = _("PostTags")

    def __str__(self):
        return "{} - {}".format(self.post, self.tag)


class TaggedUser(BaseModel):
    user = models.ForeignKey(
        User, related_name="tagged_posts", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name="tagged_users", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("TaggedUser")
        verbose_name_plural = _("TaggedUsers")

    def __str__(self):
        return "{} - {}".format(self.user, self.post)