from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=300)
    completed = models.BooleanField(null=True, default=None)
    url = models.CharField(max_length=300, null=True, default=None)
    order = models.IntegerField(null=True, default=None)
