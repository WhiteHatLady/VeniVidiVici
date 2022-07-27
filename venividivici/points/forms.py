from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from modelsDb.models import *
from django.contrib.auth.models import User,Group
from django.forms.widgets import CheckboxSelectMultiple



class PointsForm(forms.ModelForm):
    class Meta:
        model = Points
        fields = "__all__"