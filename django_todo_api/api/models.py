from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=300)
    completed = models.BooleanField()
    url = models.CharField(max_length=300)
    order = models.IntegerField()