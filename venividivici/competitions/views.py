from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from modelsDb.models import *
from django.shortcuts import redirect
from datetime import datetime, timedelta, timezone, tzinfo

# Create your views here.

@login_required(login_url='/points/login/')
def competitionList(request):
	competition = Competition.objects.all().order_by('id').reverse()
	# users = UserProfile.objects.all()
	# punkty = []
	# for p in points:
	# 	tttt= {}
	# 	for u in users:
	# 		if p.name == u.name:
	# 			ttt.append(p.points)
	# 	punkty[p.name] = ttt.sume# to

	context = {'competition':competition}   # 'punkty':punkty
	return render(request, 'competitionList.html', context)

@login_required(login_url='/points/login/')
def competitionDetails(request,pk):
	competition = Competition.objects.all().order_by('id').reverse().get(id=pk)
	# competition = Competition.objects.get(id=pk)
	# competition2 = []
	# if competition2.id = competition
	# 	competition2 = Competition.objects. get(competition.description)
	context = {'competition':competition}
	return render(request, 'competitionDetails.html', context)

# def competitionDelete(request, pk):
# 	point = Competition.objects.get(id=pk)
# 	if request.method == "POST":
# 		point.delete()
# 		return redirect('/points/list/')
# 	context = {'item': point}
# 	return render(request, 'pointDelete.html', context)

	
	
