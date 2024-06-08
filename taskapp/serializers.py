from rest_framework import serializers
from .models import ScrapingJob

class ScrapingJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapingJob
        fields = ['job_id', 'created_at', 'completed', 'data']
