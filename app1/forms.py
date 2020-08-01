from django import forms
from .models import Chapter,Comment,Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','slug','author','body']


class ChapterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ChapterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Chapter
        #fields = '__all__'
        fields = ['slug','chapter','chapter_name','body','attachment','active']


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ['name','comment','attachment','slug']