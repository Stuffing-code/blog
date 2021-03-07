from django import forms

from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': 'Post', 'title': 'Title'}
        title = {"title": forms.CharField(max_length=100) }
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
