from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Exhaustacion


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class ExhaustacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exhaustacion
        fields = ['floatvalue']
