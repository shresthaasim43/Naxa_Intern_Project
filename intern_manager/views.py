from django.shortcuts import render

from .models import Task, Attendence
from .serializers import TaskSerializer, AttendenceSerializer
from rest_framework import viewsets

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AttendenceViewSet(viewsets.ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer


