from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from modelsDb.models import *
from django.shortcuts import redirect
from datetime import datetime, timedelta, timezone, tzinfo


# Create your views here.


@login_required(login_url='/points/login/')
def shopAwards(request):
	user = request.user
	competitionTrue = Competition.objects.filter(saldo=True)
	mainSaldo = {}
	for c in competitionTrue:
	  for point in Points.objects.all():
	    if point.competitions == c:
	        if point.user.username_field not in mainSaldo.keys():
	          mainSaldo[point.user.username_field]=0
	        mainSaldo[point.user.username_field]+=point.points
	
	point = Points.objects.all()
	userSaldo = mainSaldo[user.username_field]
	print(userSaldo)		
	context = {"userSaldo":userSaldo,  "competitionTrue": competitionTrue}
	return render(request, 'shopAwards.html', context)