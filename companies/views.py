# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tidalapi
from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from my_django_site.decorators import *
import re
import json
from rest_framework import permissions
from .serializers import *
from django.core import serializers
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime
from django.core.mail import mail_admins
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from .forms import *
from rest_framework import mixins
#from django_filters.rest_framework import DjangoFilterbackend
from .models import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from my_django_site.decorators import first_decorater

from django.http import JsonResponse
##########################STARTS########################################################################
class CustomSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

@method_decorator(first_decorater,name='dispatch')
class Detailed_view(generics.RetrieveUpdateDestroyAPIView):
    """
    This view should return a specific instance from stocks's model
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StocksList(generics.ListCreateAPIView):
    """
     This view should return a list of all the Stock Objects
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = CustomSetPagination

class Real_state_filters(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomSetPagination
    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return realestatedata.objects.filter(user=user)
    def get_queryset(self):
        """
        by filtering against a `username` query parameter in the URL.
        """
        queryset = realestatedata.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


class Get_single_Instaance_update(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Search_filtering_backend(generics.ListAPIView):
    queryset = realestatedata.objects.all()
    serializer_class = CustomSerializer
    pagination_class = CustomSetPagination
    filter_backends=(OrderingFilter,SearchFilter)
    filterset_fields = ('street', 'city', 'zip','user__username','user__is_staff') #by filtering against username u need to pass this (user__username) in the url
    search_fields = ('user__username','user__first_name')
    ordering_fields = ('city','user__username')

class Model_Viewsets_(viewsets.ModelViewSet):
    ###here by using model view set it automatically creates router for delete/get/put/post methods for using this methods against single instance as get,put,delete you just need to pass id into the url  
    queryset= realestatedata.objects.all()
    serializer_class = CustomSerializer
    pagination_class = CustomSetPagination
    lookup_field = 'id'

    @action(detail=True,methods=['GET'])
    def Cities_Get(self,request,id=None):
        city = self.get_object()     ##it gets the city name & then furthure filter it will city 
        state_obj = realestatedata.objects.filter(city=city)
        serializer=CustomSerializer(state_obj,many=True)
        return Response (serializer.data,status=200)

    @action(detail=True,methods=['POST'])
    def Cities_Post(self,request,id=None):
        city = self.get_object()
        data =request.data
        data['city'] = city.id
        serializer = CustomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=201)
        return Response(serializer.errors , status=400)

#############################CLASS BASED VIEWS HERE ONLY ##############################################
@api_view(['GET'])
def user_count_view(request, format=None):
    user_count = User.objects.filter(is_active=True).count()
    content = {'user_count': user_count}
    return Response(content)
#FIRST VIEW HERE
def firs_view(request):
   print('IN FIRST FUNCTION')
   today = datetime.now().date()
   time=datetime.now().strftime('%H:%M:%S')
   print('TIME>>>>',time)
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "firtswelcome.html", {'todaydict':today,'daysweek':daysOfWeek})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def test_view(request):
   queryset=Stock.objects.all()
   query_=serializers.serialize('json',queryset)
   return HttpResponse(query_,content_type="application/json")

def redirect_view(request):
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return redirect("https://www.djangoproject.com")

def sendAdminsEmail(request):
   res = mail_admins('my subject', 'site is going down.first testing email to admin')
   print('Send Email')
   return HttpResponse('Mail Sent To Admin')

class Staticview(TemplateView):
    template_name = 'firststatic.html'

def signupform(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            return render(request, 'result.html', {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
            })

        else:
            form = SignupForm()
        return render(request, 'signupform.html', {'form': form})

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password_ = request.POST.get('password')
        User.objects.create_user(username=name,email=email,password=password_)
        context = {
            'name': name,
            'email': email
        }

        return  render("showdata.html", RequestContext(request, (context)))
    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
def insert(request):
    if request.method == 'POST':
        name=request.data['username']
        email=request.data['email']
        password=request.data['password']
        User.objects.create_user(username=name,email=email,password=password)
        return HttpResponse('index.html')
    else:
        return redirect('getdata')

@api_view(['GET'])
def annotation_obj(request):
    q =realestatedata .objects.annotate(Count('city')).values_list('city') #annotation
    q=realestatedata.objects.values('city').distinct().order_by()  #getting distinct values only
    qs1 = realestatedata.objects.values_list('city')
    qs2 = Stock.objects.values_list('ticker')
    #print('QUERY',q)
    q=qs1.union(qs2)
    return Response({'Results':q})


@api_view(['GET'])
def blog_get(request,id):
    if request.method == 'GET':
        stocks=richtext_field_test.objects.filter(id=id).values_list('description')
        stocks_split = str(stocks)[13:-5]
        # print('RESULTS>>>',stocks_split)
        stocks_ =re.escape(r'\r\n+')
        return render(request, 'blog_template.html', {'query': stocks_split,})


def SaveProfile(request):
    saved = False
    if request.method == "POST":
        print('IN POST REQUEST...')
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved = True
    else:
        MyProfileForm = ProfileForm()
    return render(request, 'saved.html', locals())

@cache_page(60 * 15)
def cookie_func(request,id):
    response=HttpResponse('Setting up cookies against requested id.....%s'%id)
    response.set_cookie('id',id)
    request.session['id']=id
    return response
def cookies_available(request):
    id=''
    session_value=''
    if 'id' in request.COOKIES:
        id=request.COOKIES['id']

    if 'id' in request.session:
        session_value=request.session['id']
    return render(request,'gte_cookies.html',{'id':id,'session_value':session_value})


@api_view(['GET'])
def customserialization(request,id):
    if request.method == 'GET':
        stockc=realestatedata.objects.get(pk=id)
        serializer = CustomSerializer(stockc)
        return Response(serializer.data)


@api_view(['GET'])
def users_get(request):
    if request.method == 'GET':
        stocks=User.objects.all()
        serializer=StockSerializer(stocks,many=True)
        return Response(serializer.data)

def bootstrap_signup_user(request):
    if request.method == "POST":
        print('IN POST REQUEST...bootstrap_signup')
        email=request.POST.get('email')
        name=request.POST.get("user")
        password=request.POST.get("pswd")
        print('VALUES>>>>',email,name,password)
        User.objects.create_user( email=email,username=name, password=password)
        return render(request, 'bootstrap_welcome.html', {'username': name})
    else:
        #
        print('IN VALID REQUEST')
    return render(request, 'index.html')

#SOCIAL LOGIN HEREEEEE>>>>
def googleloginuser(request,code):
    return Response({'results':code})



@api_view(['GET'])
def first_notifications(request,reciver,sender):
    print('USERNAME>>>',reciver,sender)
    if request.method == 'GET':
        user_reciver = User.objects.get(username=reciver)
        user_sender=User.objects.get(username=sender)
        notify.send(user_sender,recipient=user_reciver, actor=user_sender,verb='MY ACTUAL NOTIfication', nf_type='followed_by_one_hassan')
        return Response('notiofication generated')



@api_view(['POST'])
def form_submitting(request):
    if request.method == 'POST':
        name = request.data['username']
        email = request.data['email']
        password_ = request.data['password']
        User.objects.create_user(username=name, email=email, password=password_)
        return Response("User Registered...")
    else:
        return Response("Bad Request....")

@api_view(['GET','PUT','DELETE'])
def user_put_del_angular(request,username):
    user_info=''
    try:
        user_info = User.objects.get(username=username)
    except:
        pass
    if request.method == 'GET':
       serializer=UserSerializer(user_info)
       return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserSerializer(user_info,request.data)
        print('FilterRES>>>', user_info)
        if serializer.is_valid():
           serializer.save()
        return Response('DATA UPDATED',status=status.HTTP_202_ACCEPTED)
    return  Response('ERRORS',status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def Getmusic(request):
    print('hello view')
    session = tidalapi.Session()
    session.login('username', 'password')
    tracks = session.get_album_tracks(album_id=16909093)
    for track in tracks:
        print(track.name)