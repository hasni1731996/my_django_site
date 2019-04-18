from rest_framework import serializers
from .models import *

class SongsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields= ('file_type','song_title')

class AlbumSerializers(serializers.ModelSerializer):
    album_musician= SongsSerializers(many=True)
    class Meta:
        model = Album
        fields=('artist','album_title','album_logo','album_musician')

    def create(self, validated_data):
        album_data = validated_data.pop('album_musician')
        album = Album.objects.create(**validated_data)
        for song_data in album_data:
            Song.objects.create(album=album, **song_data)
        return album

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album_title = validated_data.get('album_title', instance.album_title)
        instance.genre = validated_data.get('genre',instance.genre)
        instance.album_logo = validated_data.get('album_logo',instance.album_logo)
        instance.save()

        for album_data in albums_data:
            album = albums.pop(0)
            album.file_type = album_data.get('file_type', album.file_type)
            album.song_title = album_data.get('song_title', album.song_title)
            album.save()
        return instance