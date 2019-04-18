from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = ('title', 'artists')

class ArtistSerializer(serializers.ModelSerializer):
    artistmovie=MovieSerializer(many=True)
    class Meta:
        model = artist
        fields = ('name','artistmovie')


class RoleSerializer(serializers.ModelSerializer):
    artist=ArtistSerializer()
    class Meta:
        model = role
        fields = ('role_name','artist')
