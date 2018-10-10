from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import ResourceSerializer
from .models import Resource

class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resources to be viewed or edited.
    """
    permission_classes = (IsOwner,)
    queryset = Resource.objects.all().order_by('-create_time')
    serializer_class = ResourceSerializer

    def list(self, request):
        queryset = Resource.objects.filter(owner=request.user).order_by('-create_time')
        serializer = ResourceSerializer(queryset, many=True)
        return Response(serializer.data)
