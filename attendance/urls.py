from django.urls import path
from .views import (
    # AttendanceListView,
    AttendanceDetailView,
    AttendanceUpdateView,
    AttendanceDeleteView,
    AttendanceCreateView,
    attendance_eligible
    )


urlpatterns = [
    path('<int:pk>/edit/', AttendanceUpdateView.as_view(), name='attendance_edit'),
    path('<int:pk>/', AttendanceDetailView.as_view(), name='attendance_detail'),
    path('<int:pk>/delete', AttendanceDeleteView.as_view(), name='attendance_delete'),
    path('new/', AttendanceCreateView.as_view(), name='attendance_new'),
    # path('', AttendanceListView.as_view(), name='attendance_list'),
    path('', attendance_eligible, name='attendance_list'),
]