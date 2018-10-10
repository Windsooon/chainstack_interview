from rest_framework import serializers
from rest_framework.response import Response
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'unique_id', 'create_time')

    def create(self, validated_data):
        user =  self.context['request'].user
        if user.quota:
            if user.quota <= 1:
                return Response(status=400)
            else:
                user.quota -= 1
                user.save()
        validated_data['owner'] = user
        return Resource.objects.create(**validated_data)
