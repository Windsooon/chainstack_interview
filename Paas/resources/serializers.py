from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'unique_id', 'create_time')

    def create(self, validated_data):
        user =  self.context['request'].user
        validated_data['owner'] = user
        return Resource.objects.create(**validated_data)
