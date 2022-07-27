from django.db import models
from django.utils import timezone
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from datetime import date
from datetime import datetime
from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from django.db.models import Sum

class UserProfileManager(BaseUserManager):
	"""Manager for user profiles"""

	def create_user(self, email, name, password=None):
		"""Create a new user profile"""
		if not email:
			raise ValueError('Users must have an email address')

		email = self.normalize_email(email)
		user = self.model(email=email, name=name,)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""Create and save a new superuser with given details"""
		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db) 

		return user



class Group(models.Model):
	id 		= models.AutoField(primary_key=True)
	name	= models.CharField(_('Rodzaj tytanów') ,max_length=200)
	text    = models.TextField(_('Opis'))
	def __str__(self):
		return self.name

class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Database model for users in the system"""
	id 				= models.AutoField(primary_key=True)
	email 			= models.EmailField(max_length=255)
	username_field 	= models.CharField(max_length=255, unique=True)
	name 			= models.CharField(max_length=255, unique=True)
	surname 		= models.CharField(max_length=255)
	position 		= models.CharField(max_length=255,default=False)
	is_manager 		= models.BooleanField(default=False)
	is_active 		= models.BooleanField(default=True)
	is_staff 		= models.BooleanField(default=False)
	group 			= models.ManyToManyField(Group, verbose_name=_('Grupa'), null=True)

	objects = UserProfileManager()

	USERNAME_FIELD = 'name'
	REQUIRED_FIELDS = ['email']

	def get_full_name(self):
		"""Retrieve full name for user"""
		return self.name

	def get_short_name(self):
		"""Retrieve short name of user"""
		return self.name

	def __str__(self):
		"""Return string representation of user"""
		return (self.name+' '+self.surname)


# class Category(models.Model):
# 	name 			= models.CharField(_('Opis'),max_length=200)
# 	def __str__(self):
# 		return self.name


# class UsersToGroup(models.Model):
# 	group 			= models.ForeignKey(Group, verbose_name=_('Grupa'), null=True, on_delete = models.CASCADE)
# 	user 			= models.ForeignKey(UserProfile, verbose_name=_('Grupa'), null=True, on_delete = models.CASCADE)


class Competition(models.Model):
	id 				= models.AutoField(primary_key=True)
	title			= models.CharField(_('Nazwa rywalizacji') ,max_length=200)
	description		= models.TextField(_('Opis rywalizacji') , default='')
	group 			= models.ManyToManyField(Group, verbose_name=_('Grupa'), null=True)
	date_start 		= models.DateTimeField(_('Data rozpoczęcia'),auto_now=False, null=True, default=datetime.now())
	date_end 		= models.DateTimeField(_('Data zakończenia'),auto_now=False, null=True, default=datetime.now())
	saldo 			= models.BooleanField(default=True)

	def __str__(self):
		return self.title


class Points(models.Model):
	description		= models.CharField(_('Quest'),max_length=200)
	points		 	= models.IntegerField(_('EXP'), default=1)
	user 			= models.ForeignKey(UserProfile, verbose_name=_('Tytani'), null=True, on_delete = models.CASCADE)
	competitions	= models.ForeignKey(Competition, verbose_name=_('Rywalizacje'), null=True, on_delete = models.CASCADE)
	date 			= models.DateTimeField(_('Data utworzenia'),auto_now=False, null=True, default=datetime.now())
	mainPoints		= models.IntegerField(_('Punkty do salda głównego'), default=0)
	def __str__(self):
		return self.description
	

class Rules(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    # def publish(self):
    # self.published_date = timezone.now()
    # self.save()

    def __str__(self):
        return self.title


class Shop(models.Model):
	id 			= models.AutoField(primary_key=True)
	item		= models.CharField(_('Nazwa') ,max_length=200)
	description	= models.CharField(_('Opis'),max_length=200)
	points 		= models.IntegerField(('Punkty'),)

	def __str__(self):
		return self.item	


class Hof(models.Model):
	id 			= models.AutoField(primary_key=True)
	user 		= models.ForeignKey(UserProfile, verbose_name=_('Tytani'), null=True, on_delete = models.CASCADE)
    # points 		= models.ManyToManyField(Points)


	def __str__(self):
		return self.id

	# def sumPoint(self):
 #    	return sum(points.all())
