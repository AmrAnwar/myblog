from django import forms
from . models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    """docstring for PostForm """
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        """docstring for Meta"""
        model = Post
        fields = [
            "title",
            "content",
            "wait",
            "image",
            "type"
        ]