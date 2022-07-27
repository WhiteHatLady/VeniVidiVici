from django.urls import path, include
from hof import views

urlpatterns = [
	# path('login/', views.loginPage, name='login'),
	# path('logout/', views.logoutUser, name='logout'),
	# path('home/', views.home, name='home'),

	path('list/', views.hofList,  name='hofList'),
	# path('new/', views.pointNew, name='pointNew'),
	# path('new/<str:pk>', views.pointDelete, name='pointDelete'),
	# path('edit/<str:pk>', views.pointEdit, name='pointEdit'),

]