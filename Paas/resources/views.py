from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ResourceSerializer
from .models import Resource

class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resources to be viewed or edited.
    """
    queryset = Resource.objects.all().order_by('-create_time')
    serializer_class = ResourceSerializer
