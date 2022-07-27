from django.urls import path, include
from rules import views
from .views import home
urlpatterns = [
	path('list/', views.rulesList, name='rulesList'),
	path('new/', views.rulesNew, name='rulesNew'),
	#path('edit/<str:pk>', views.rulesList, name='rulesList'),

]