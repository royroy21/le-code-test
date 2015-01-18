from django.db import models
from django.contrib.auth.models import User


class ItemAbstract(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class PhotoItem(ItemAbstract):
    image = models.ImageField(upload_to='media/')
    active = models.BooleanField(default=True)


class TweetItem(ItemAbstract):
    text = models.CharField(max_length=150)
    active = models.BooleanField(default=True)