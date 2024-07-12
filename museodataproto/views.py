from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})