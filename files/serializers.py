from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'uploaded_at', 'status', 'progress', 'result_summary']
        read_only_fields = ['status', 'progress', 'result_summary', 'uploaded_at']