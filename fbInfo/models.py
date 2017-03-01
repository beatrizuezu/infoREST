from django.db import models


class UserFb(models.Model):
    username = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    fb_id = models.CharField(max_length=128, unique=True)
    gender = models.CharField(max_length=8)
