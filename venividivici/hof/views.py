from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from modelsDb.models import *
from django.shortcuts import redirect
from datetime import datetime, timedelta, timezone, tzinfo
from django.db.models import Sum

# Create your views here.


def hofList(request):
	competition = Competition.objects.all().order_by('id').reverse()
	# competition = Competition.objects.all().order_by('id')
	# users = UserProfile.objects.all()
	# punkty = []
	# for p in points:
	# 	tttt= {}
	# 	for u in users:
	# 		if p.name == u.name:
	# 			ttt.append(p.points)
	# 	punkty[p.name] = ttt.sume# to

	context = {'competition':competition}   # 'punkty':punkty
	return render(request, 'hofList.html', context)



# punkty = {}

# competition = Competition.objects.all()[1]
# for point in Points.objects.filter(competitions=competition):
#  if point.user.username_field not in punkty.keys():
#   punkty[point.user.username_field]=0
#  punkty[point.user.username_field]+=point.points



#  # powiązanie 
#  competition = Competition.objects.get(id=1)[1]

# Próba podliczenia wszystkich punktów - teraz sumuje wszystkie punkty wszystkich uczestników 
# p1 jest słownikiem
# p1 = Points.objects.aggregate(total_score=Sum('points'))
# p1
#wynik który wyszedł
# {'total_score': 86}

# wyciągniecie samego wyniku:
 # p1['total_score']

# def funkcja():
# ...     t2 = 0
# ...     users2 = UserProfile.objects.all()
# ...     for u in users2:
# ...             if u == 'Magdalena Powałowska':
# ...                     dictT2 = Points.objects.aggregate(total_score=Sum('points'))



#  def funkcja():
# ...     t2 = 0
# ...     users2 = UserProfile.objects.all()
# ...     for u in users2:
# ...             if u == 'Magdalena Powałowska':
# ...                     dictT2 = Points.objects.aggregate(total_score=Sum('points'))
# ...                     t2 = t2 + dictT2['total_score']
# ...     return t2


#!!!!!!!!!  NA RAZIE FUNKCJA NADAL OBLICZA WSZYSTKIE PUNKTY, a nie tylko dla konkretnego usera
# def suma():
# ...     sumaSingleUser = 0
# 		allUsers = UserProfile.objects.all()
# 		length = len(allUsers)
# 		for x in range(1,length):
# 			singleUser = UserProfile.objects.get(id=x)
# 			singleUserName = singleUser.username_field
# 			# username = singleUser.username_field
# ...       if singleUserName == 'magdalenap':
# 					sumaSingleUser = 0
# ...               sumaDict = Points.objects.aggregate(total_score=Sum('points'))
# ...               sumaSingleUser = sumaSingleUser + sumaDict['total_score']
# 					return sumaSingleUser

