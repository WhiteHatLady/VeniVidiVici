from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from . import urls
from . import views
from points import views
from points import urls
from rules import views
from django.contrib.auth.decorators import login_required

# Create your views here.

# https://www.youtube.com/watch?v=P6QHswl2PqE   How to do change password. 
class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy(views.home)