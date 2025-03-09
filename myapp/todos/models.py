from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Todo(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.now)
    last_updated = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title
