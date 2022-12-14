# Generated by Django 4.0.4 on 2022-07-26 12:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('username_field', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('surname', models.CharField(max_length=255)),
                ('position', models.CharField(default=False, max_length=255)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Nazwa rywalizacji')),
                ('description', models.TextField(default='', verbose_name='Opis rywalizacji')),
                ('date_start', models.DateTimeField(default=datetime.datetime(2022, 7, 26, 14, 10, 57, 668712), null=True, verbose_name='Data rozpocz??cia')),
                ('date_end', models.DateTimeField(default=datetime.datetime(2022, 7, 26, 14, 10, 57, 668727), null=True, verbose_name='Data zako??czenia')),
                ('saldo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Rodzaj tytan??w')),
                ('text', models.TextField(verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=200, verbose_name='Nazwa')),
                ('description', models.CharField(max_length=200, verbose_name='Opis')),
                ('points', models.IntegerField(verbose_name='Punkty')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Quest')),
                ('points', models.IntegerField(default=1, verbose_name='EXP')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 7, 26, 14, 10, 57, 669436), null=True, verbose_name='Data utworzenia')),
                ('mainPoints', models.IntegerField(default=0, verbose_name='Punkty do salda g????wnego')),
                ('competitions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelsDb.competition', verbose_name='Rywalizacje')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Tytani')),
            ],
        ),
        migrations.CreateModel(
            name='Hof',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Tytani')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='group',
            field=models.ManyToManyField(null=True, to='modelsDb.group', verbose_name='Grupa'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='group',
            field=models.ManyToManyField(null=True, to='modelsDb.group', verbose_name='Grupa'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
