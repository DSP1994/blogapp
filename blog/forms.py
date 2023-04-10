from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    content = forms.CharField()

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'image', 'content', 'status')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': '*Actual text is required'}
