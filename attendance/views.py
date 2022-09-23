from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Attendance


# class AttendanceListView(LoginRequiredMixin, ListView):

    # model = Attendance
    # template_name = 'attendance_list.html'


    # def get_context_data(self, **kwargs): 
    #     kwargs = super().get_context_data()
    #     count_true = Attendance.objects.all().filter(present=True).count()
    #     count_false = Attendance.objects.all().filter(present=False).count()
    #     total_count = count_true + count_false
    #     percentage_present = (count_true/total_count) * 100
    #     percentage_present = int(percentage_present)
    #     kwargs.update(percentage_present)
    #     return kwargs


    # def get_queryset(self, *args, **kwargs):
    #     if self.request.user.is_superuser:
    #         qs = Attendance.objects.all()
    #         return qs
    #     else:
    #         qs = Attendance.objects.all()
    #         qs = qs.filter(student=self.request.user)
    #         return qs

    

class AttendanceCreateView(LoginRequiredMixin,CreateView):
     
    model = Attendance
    template_name = 'attendance_new.html'
    fields = ('subject', 'summary', 'present',)

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super(AttendanceCreateView, self).form_valid(form) 



class AttendanceDetailView(LoginRequiredMixin, DetailView):
    model = Attendance
    template_name = 'attendance_detail.html'
    

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            qs = Attendance.objects.all()
            return qs
        else:
            qs = Attendance.objects.all()
            qs = qs.filter(student=self.request.user)
            return qs



class AttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Attendance
    fields = ('subject', 'summary',)
    template_name = 'attendance_edit.html'


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.student != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class AttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'attendance_delete.html'
    success_url = reverse_lazy('attendance_list')

    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


@login_required
def attendance_eligible(request):
    object_list = Attendance.objects.filter(student=request.user)
    true_count = object_list.filter(present=True).count()
    false_count = object_list.filter(present=False).count()
    total_count = true_count + false_count
    percentage_present  = (true_count/total_count) * 100

    if request.user.is_superuser:
        object_list = Attendance.objects.all()

    context = {'object_list':object_list, 'percentage_present':percentage_present}

    return render(request, 'attendance_list.html', context=context)