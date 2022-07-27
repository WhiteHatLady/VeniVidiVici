from django.urls import path, include
from competitions import views

urlpatterns = [
	# path('login/', views.loginPage, name='login'),
	# path('logout/', views.logoutUser, name='logout'),
	# path('home/', views.home, name='home'),

	path('list/', views.competitionList, name='competitionList'),
	path('details/<str:pk>', views.competitionDetails, name='competitionDetails'),

	# path('new/', views.pointNew, name='pointNew'),
	# path('new/<str:pk>', views.pointDelete, name='pointDelete'),
	# path('edit/<str:pk>', views.pointEdit, name='pointEdit'),

]