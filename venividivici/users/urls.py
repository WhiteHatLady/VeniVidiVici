from django.urls import path
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views
urlpatterns = [
	#path('password/', auth_views.PasswordChangeView.as_view(template_name ='userprofile/change-password.html'),),
	path('password/', PasswordsChangeView.as_view(template_name ='userprofile/change-password.html'), name="change-password"),
]