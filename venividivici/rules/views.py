from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from modelsDb.models import *
from points.forms import * 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	context = {}
	return redirect('/points/list/')

@login_required(login_url='/points/login/')
def rulesList(request):
	rules = Rules.objects.all()
	context = {'rules':rules}
	return render(request, 'rulesList.html', context)

@login_required(login_url='/points/login/')
def rulesNew(request):
	rules = Rules.objects.all()
	context = {'rules':rules}
	return render(request, 'rulesList.html', context)