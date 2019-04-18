# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.views import View
from rest_framework.views import APIView
from django.contrib.auth.models import User
from my_django_site import settings
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Userchat
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import datetime
class Fist_view_template(TemplateView):
    template_name = "chat/login.html"
    def post (self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(username=username, password=password)
        c = User.objects.all().exclude(username=username)
        print(c)
        if user is not None:
            return render(request,"chat/first.html",{'username':username,'chat': c})
        else:
            return HttpResponse('error here')

# class Welcome_User(APIView):
#     print('In Post request Here')
#     def post(self, request, format=None):
#         username =request.data('username')
#         password = request.data('password')
#         return HttpResponse('error here')
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class message_Template(TemplateView):
    template_name = "chat/first.html"
    def post(self, request):
        print('in post request message')
        sender = request.POST('sender')
        reciver = request.POST('reciver')
        message=request.POST('message')
        print(sender,reciver)