from rest_framework import serializers
from .models import ZenoCsv, ZenoUpload


class ZenoCsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZenoCsv
        fields = ['idd', 'timestamp', 'temperature', 'duration']


class ZenoCsvUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZenoUpload
        fields = "__all__"
