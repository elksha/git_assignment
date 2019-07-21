from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm, UserForm
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
    else:
        form = UserForm()
        error = "아이디가 이미 존재합니당"
        return render(request, 'registration/signup.html', {'form': form, 'error': error})

# Create your views here.
