from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    note = models.CharField(max_length=64, blank=True, null=True, default=None)
    date_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)