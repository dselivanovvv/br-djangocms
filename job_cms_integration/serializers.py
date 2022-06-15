from rest_framework import serializers

from job.serializers import JobSerializer
from job_cms_integration.models import JobPluginModel


class JobIntegrationSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True)

    class Meta:
        model = JobPluginModel
        fields = '__all__'
