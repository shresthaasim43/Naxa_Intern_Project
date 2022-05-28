from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile, Task, Attendence

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = '__all__'
