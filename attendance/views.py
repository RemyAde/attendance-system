from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from users.models import CustomUser

from .models import Attendance


class AttendanceListView(LoginRequiredMixin, ListView):

    model = Attendance
    template_name = 'attendance_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = Attendance.objects.all()
        qs = qs.filter(student=self.request.user)
        return qs


