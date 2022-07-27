from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from modelsDb.models import *
from points.forms import * 
from django.shortcuts import redirect
from datetime import datetime, timedelta, timezone, tzinfo
from django.contrib import messages



# https://medium.com/djangotube/django-roles-groups-and-permissions-introduction-a54d1070544
def loginPage(request):
	print("============================================================")
	print("============================================================")
	print("============================================================")
	print(request.POST) 
	
	if request.method == "POST":
		Usr = get_user_model()
		# print(Usr)
		username = request.POST.get("username").strip()
		# print(username)
		# print(request.POST)
		u = Usr.objects.filter(username_field=username)
		if len(u) > 0:
			password = request.POST.get("password")
			#print(password)
			user = Usr.objects.get(username_field=username)
			#print(user)
			check = user.check_password(password)
			#print(check)
			if user is not None and user.check_password(password):
				# if user.is_colored
				login(request, user)
				return redirect('/points/list/')
			else:
				messages.info(request,'Użytkownik lub hasło jest nieprawidłowe!')
				return redirect('/points/login/')
		else:
			messages.info(request, 'Użytkownik lub hasło jest nieprawidłowe!')
			return redirect('/points/login/')
	context = {}
	return render(request, 'login.html', context)


@login_required(login_url='/points/login/')
def logoutUser(request):
	logout(request)
	return redirect('login')


# @login_required(login_url='login')
@login_required(login_url='/points/login/')
def home(request):
	context = {}
	return render(request, 'home.html', context)


@login_required(login_url='/points/login/')
def pointList(request):
	current_user = request.user
	if current_user.is_superuser:
		points = Points.objects.all().order_by('id').reverse()
	else:
		points = Points.objects.filter(user=current_user).order_by('id').reverse()	
	# users = UserProfile.objects.all()
	# punkty = []
	# for p in points:
	# 	tttt= {}
	# 	for u in users:
	# 		if p.name == u.name:
	# 			ttt.append(p.points)
	# 	punkty[p.name] = ttt.sume# to

	context = {'points':points}   # 'punkty':punkty
	return render(request, 'pointList.html', context)

@login_required(login_url='/points/login/')
def pointEdit(request,pk):
	try:
		# dupa = "dupa"
		# dupy = ['ładna', 'zgrabna', 'brudna']
		points = Points.objects.get(id=pk)
		form = PointsForm(instance=points)
		if request.method == "POST":
			form = PointsForm(request.POST, instance=points)
			if form.is_valid():
				form.save()
				return redirect('/points/list/')
		context = {"form": form, "pk": pk,} #"dupa":dupa,"dupy":dupy
		return render(request, 'pointEdit.html', context)

	except ObjectDoesNotExist:
		print("Oops!", sys.exc_info()[0], "occurred.")
		messages.warning(request,'Wrong ID')
		return redirect('/points/list/')
		pass


@login_required(login_url='/points/login/')
def pointNew(request):
	form = PointsForm()
	if request.method == "POST":
		form = PointsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/points/list/')

	context = {'form': form}
	return render(request, 'pointCreate.html', context)


@login_required(login_url='/points/login/')
def pointDelete(request, pk):
	point = Points.objects.get(id=pk)
	if request.method == "POST":
		point.delete()
		return redirect('/points/list/')
	context = {'item': point}
	return render(request, 'pointDelete.html', context)

# Punkty podliczane każdemu użytkownikowi z pierwszej kategorii. 

@login_required(login_url='/points/login/')
def pointScore(request, pk):
	# competitionAll = Competition.objects.all()[1]
	competition = Competition.objects.all().order_by('id').get(id=pk)
	# competitionAll = Competition.objects.all()
	# competition = Competition.objects.get(id=1)
	addToMainPoints = Competition.objects.filter(saldo=True)
	punkty = {}
	sumna = {}
	# saldo = {}
	# if superadmin
	for point in Points.objects.filter(competitions=competition):
	 	if point.user.username_field not in punkty.keys():
	 		punkty[point.user.username_field]=0
	 	# if 	Points.objects.filter(competitions=addToMainPoints):
	 	punkty[point.user.username_field]+=point.points

	# for competitionTrue in addToMainPoints:
	#     for point in Points.objects.filter(competitions=competition):
	#     	if competitionTrue == competition:
	#     		if point.user.username_field not in mainSaldo.keys():
	# 	        	mainSaldo[point.user.username_field]=0
	# 			mainSaldo[point.user.username_field]+=punkty[point.user.username_field]
	# print(mainSaldo) 

	punkty = {k: v for k, v in sorted(punkty.items(), key=lambda item: item[1], reverse=True)}
	context = {'punkty': punkty, 'competition':competition}
	return render(request, 'pointScore.html', context)


# saldo główne - punkty do wydania w sklepie


@login_required(login_url='/points/login/')
def pointSaldo(request):
	user= request.user

	competitionTrue = Competition.objects.filter(saldo=True)
	mainSaldo = {}
	for c in competitionTrue:
	  for point in Points.objects.all():
	    if point.competitions == c:
	        if point.user.username_field not in mainSaldo.keys():
	          mainSaldo[point.user.username_field]=0
	        mainSaldo[point.user.username_field]+=point.points
	print(mainSaldo)
	context = {"mainSaldo":mainSaldo, "competitionTrue": competitionTrue}
	return render(request, 'shopAwards.html', context)




# for p in point:



# 	for pk in competition.id
# 	Points.objects.filter(competitions = "pk")
# 	point = Points.objects.all()
# 	userlist = UserProfile.objects.all()
# 	competition = Comp.objects.all()
# 	sum = 0
# 	for u in point.user:
# 		for c in point.competition
# 			sum = sum + point.points
# 			return sum 
# 	context = {'item': point}
# 	return render(request, 'pointScore.html', context)




