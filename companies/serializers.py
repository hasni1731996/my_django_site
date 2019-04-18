from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=richtext_field_test
        fields=('description',)


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = realestatedata
        fields = ('city', 'zip')

class UserSerializer(serializers.ModelSerializer):
    userstate=CustomSerializer(many=True)
    class Meta:
        model =  User
        fields = ('username' , 'email','userstate')
        extra_kwargs = {'username': {'validators': [],},}

    def create(self, validated_data):
        state_data = validated_data.pop('userstate')
        user = User.objects.create(**validated_data)
        for data_state in state_data:
            realestatedata.objects.create(user=user, **data_state)
        return user

    def update(self, instance, validated_data):
        states_data = validated_data.pop('userstate')
        real_data = (instance.userstate).all()
        real_data = list(real_data)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        for data in states_data:
            album = real_data.pop(0)
            album.zip = data.get('zip', album.zip)
            album.city = data.get('city', album.city)
            album.save()
        return instance