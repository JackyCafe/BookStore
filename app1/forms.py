from django import forms
from .models import Chapter


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['name','chapter','body','attachment']

