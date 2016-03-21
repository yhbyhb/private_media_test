from django.db import models
from private_media.storages import PrivateMediaStorage

# Create your models here.
class MediaTest(models.Model):
    publicFile = models.FileField()
    privateFile = models.FileField(storage=PrivateMediaStorage())