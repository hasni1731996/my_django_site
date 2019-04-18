from django.urls import include,path
from . import  views
urlpatterns = [
    #/music/
    path('detail_views/<int:pk>/',views.detail_music_instance.as_view()),
   # path('code/(?P<album_id>[0-9]+)/', views.detail,name='detail'),
]