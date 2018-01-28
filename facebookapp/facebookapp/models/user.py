from django.db import models


class User(models.Model):
    class Meta:
        app_label = "facebookapp"

    name = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    fb_id = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
