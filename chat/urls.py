# chat/urls.py
from django.urls import path
from chat.views import *
urlpatterns = [
    path('index/', Fist_view_template.as_view()),

    # path('welcome/', Welcome_User.as_view(),name='welcome'),

    path('post_message/', message_Template.as_view()),

]