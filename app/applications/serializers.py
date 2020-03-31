from rest_framework import serializers

from applications.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'access_key']
        read_only_fields = ['id', 'access_key']


class ApplicationQueryParamSerializer(serializers.Serializer):
    access_key = serializers.UUIDField(required=True)
