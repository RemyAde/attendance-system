from django.contrib import admin

from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Attendance, AttendanceAdmin)