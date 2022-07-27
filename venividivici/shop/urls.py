from django.urls import path, include
from shop import views

urlpatterns = [
	path('awards/', views.shopAwards, name='shopAwards'),
	# path('saldo/', views.shopAwards, name='shopAwards'),

]