"""my_django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth import views
from companies.views import *
import debug_toolbar
#import notifications.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.LoginView, name='login'),
    # path('logout/', views.LogoutView, name='logout'),
    # path(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    path('music/', include('music.urls')),
    path('chat/', include('chat.urls')),
    path('company/', include('companies.urls')),
    path('test/', include('testapp.urls')),
    path('notifications/', include('notify.urls', 'notifications')),
    path(r'^__debug__/', include(debug_toolbar.urls)),
]