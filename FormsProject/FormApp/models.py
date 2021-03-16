from django.db import models

# Create your models here.
class profile(models.Model):
    firstname = models.CharField(max_length = 264)
    lastname = models.CharField(max_length = 264)
    email = models.EmailField(max_length = 264)
    feedb = models.CharField(max_length = 264)
