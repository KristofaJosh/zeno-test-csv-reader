from rest_framework import serializers
from .models import ZenoCsv


class ZenoCsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZenoCsv
        fields = ['idd', 'timestamp', 'temperature', 'duration', 'created_at', 'last_modified_at']
