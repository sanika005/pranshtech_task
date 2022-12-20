from django.db import models

class students(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    current_position = models.CharField(max_length=255)
