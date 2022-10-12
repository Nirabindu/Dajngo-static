from django.db import models

# Create your models here.


class Med(models.Model):
    images = models.ImageField(upload_to = 'media/')