from django.urls import path
from .views import AttendanceListView


urlpatterns = [
    path('', AttendanceListView.as_view(), name='attendance_list'),
]