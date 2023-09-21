from django.db import models


# Create your models here.

class apps_Upload_File(models.Model):
    file = models.ImageField(upload_to='images')
