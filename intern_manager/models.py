from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

class Task(models.Model):
    name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Attendence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendence_time = models.DateTimeField(auto_now_add=True)