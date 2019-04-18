# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from rest_framework.pagination import PageNumberPagination
from .serializers import *
class CustomSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000
class detail_music_instance(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

