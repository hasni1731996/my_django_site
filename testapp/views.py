from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .models import *
from .serializers import *

class CustomSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class test_Viewsets_(generics.ListAPIView):
    serializer_class = RoleSerializer
    pagination_class = CustomSetPagination

    def get_queryset(self):
        queryset = role.objects.all()
        artist_name = self.request.query_params.get('artist', None)
        if artist_name is not None:
            print('artist..',artist_name)
            queryset = queryset.filter(artist__name=artist_name)

        mov_name = self.request.query_params.get('mov', None)
        if mov_name is not None:
            print('mov',mov_name)
            queryset = queryset.filter(movie__title=mov_name)

        role_name = self.request.query_params.get('role', None)
        if role_name is not None:
            print('role',role_name)
            queryset = queryset.filter(role_name=role_name)
        return queryset


class prefetch_filteration(generics.ListAPIView):
    serializer_class = RoleSerializer
    pagination_class = CustomSetPagination

    def get_queryset(self):
        queryset = role.objects.select_related('movie').prefetch_related('movie__artists')
        return queryset