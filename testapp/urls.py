# chat/urls.py
from django.urls import path,include
from testapp import views

urlpatterns = [
     path('search_models_objects_',views.test_Viewsets_.as_view()),

    path('prefetch_models_objects_',views.prefetch_filteration.as_view()),
]