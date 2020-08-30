from .models import Posts
from rest_framework import serializers
from django.contrib.auth.models import User
#vhvkjdvkdjvnbdkjbssvkbdkjb dbvkjdbvkd sdbvkjsdv sdkjbkjsdb sd jksdbkjsdbvkjsdbkjsdbvkvbsdkv


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('title', 'content', 'if_featured')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =  '__all__'
