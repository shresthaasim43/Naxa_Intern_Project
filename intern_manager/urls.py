from django.urls import path,include
from rest_framework import routers
from .views import TaskViewSet, AttendenceViewSet


router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'attendence', AttendenceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]