from django.forms import ModelForm, Select
from .models import Attendance

SUBJECT_CHOICES = [
    ('MEE 411','MEE411'),
    ('MEE 412','MEE412'),
    ('MEE 413','MEE413'),
    ('MEE 414','MEE414'),
    ('MEE 415','MEE415'),
    ('MEE 416','MEE416'),
    ('MEE 417','MEE417'),
    ('MEE 418','MEE418'),
    ('MEE 419','MEE419'),
]

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ('subject', 'summary', 'present')
        widgets = {
            'subject': Select(choices=SUBJECT_CHOICES)
        }



class AttendanceUpdateForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ('subject', 'summary',)
        widgets = {
            'subject': Select(choices=SUBJECT_CHOICES),
        }