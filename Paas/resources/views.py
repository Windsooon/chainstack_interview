from django.shortcuts import render
from .serializers import ResourceSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resources to be viewed or edited.
    """
    queryset = Resource.objects.all().order_by('-create_time')
    serializer_class = ResourceSerializer
