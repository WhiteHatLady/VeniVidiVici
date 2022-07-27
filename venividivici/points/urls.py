from django.urls import path, include
from points import views

urlpatterns = [
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('home/', views.home, name='home'),
	path('list/', views.pointList, name='pointList'),
	path('new/', views.pointNew, name='pointNew'),
	path('new/<str:pk>', views.pointDelete, name='pointDelete'),
	path('edit/<str:pk>', views.pointEdit, name='pointEdit'),
	path('score/<str:pk>', views.pointScore, name='pointScore'),
	# path('saldo/', views.pointSaldo, name='pointaldo'),
	# path('main/', name='pointMain'),
]