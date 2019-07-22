from django import forms
from .models import Post
from django.contrib.auth.models import User
from .models import Post, Comment
from django import forms 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents', 'created_date', 'author')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)