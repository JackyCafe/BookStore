from django import forms
from .models import Chapter


class ChapterForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(ChapterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



    class Meta:
        model = Chapter
        fields = ['slug','chapter','body','attachment']

