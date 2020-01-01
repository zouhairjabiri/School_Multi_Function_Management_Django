from django import forms
from . import models


class addsubject(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = ['subject']
