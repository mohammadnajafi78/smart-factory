from django.contrib.auth.models import Group, User
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

from quickstart.serializers import (ExhaustacionSerializer, GroupSerializer,
                                    UserSerializer)

from .models import Exhaustacion


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# from ..serializers import (
#     AssessmentTypeListSerializer,
#     AssessmentTypeDetailSerializer,
# )

class ExhaustacionListView(ListAPIView):
    # queryset = Exhaustacion.objects.filter(tagid=25)
    serializer_class = ExhaustacionSerializer
    permission_classes = []

    def get_queryset(self):
        return (
            Exhaustacion.objects.filter(tagid=25)
        )

class GasListView(ListAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []