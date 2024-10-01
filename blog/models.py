from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=255)
