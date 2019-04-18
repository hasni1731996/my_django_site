# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from my_django_site.utils import ChoiceEnum
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Count

class Stock(models.Model):
    ticker=models.CharField(max_length=10)
    open=models.FloatField()
    close=models.FloatField()
    volume=models.IntegerField()
    def __str__(self):
        return self.ticker

class StateManager(models.Manager):
    def city_count(self, keyword):
        return self.filter(city=keyword).aggregate(Count('city' , distinct=True))

class total_state_Manager(models.Manager):
    def total_model_obj(self):
        return self.aggregate(Count('city' , distinct=True))

class realestatedata(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userstate',default=1)
    street=models.CharField(max_length=1000)
    city=models.CharField(max_length=1000)
    zip=models.CharField(max_length=1000)
    state=models.CharField(max_length=1000)
    beds=models.CharField(max_length=1000)
    baths=models.CharField(max_length=1000)
    objects = models.Manager()
    city_obj = StateManager() ####this manger return distinct queryset on the basis of the passed parameter as realestatedata.city_obj.city_count('SACRAMENTO')
    total_cities = total_state_Manager() ####this manager will returns total number of distint cities from model

    def __str__(self):
        return "%s (%s)" % (self.user.username, self.city)
class richtext_field_test(models.Model):
    description = RichTextField(blank=True, null=True)

##############Model's Managers for getting queryset according to the filed which we need to filter from querysets
#This Custom Model Managers's methods will allow us to call both methods using single manager class ####
class UsersQuerySet(models.QuerySet):
    def vendors(self):
        return self.filter(roles='VENDOR')

    def users(self):
        return self.filter(roles='USER')

class Users_Manager(models.Manager):
    def get_queryset(self):
        return UsersQuerySet(self.model, using=self._db)

    def vendors(self):
        return self.get_queryset().vendors()

    def users(self):
        return self.get_queryset().users()

######################Ends######################

class Multi_Users(models.Model):
    USER = 'USER'
    VENDOR = 'VENDOR'
    USER_CHOICES = ((USER, 'user'),(VENDOR, 'vendor'))
    roles = models.CharField(max_length=15, choices=USER_CHOICES)
    profile= models.ForeignKey('Profile', related_name='user_profile', on_delete=models.CASCADE,default=1)
    objects = models.Manager() ###it gives default model manager as we get using modelname.objects.all
    user_objects = Users_Manager()
    
    def __str__(self):
        return self.profile.name
        

class Profile(models.Model):
    name = models.CharField(max_length = 50)
    class Meta:
        db_table = "profile"

    def __str__(self):
        return self.name