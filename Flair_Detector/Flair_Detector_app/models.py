from django.db import models

# Create your models here.

class File(models.Model):
    files = models.FileField(blank=False, null=False)

