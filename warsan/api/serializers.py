from rest_framework import serializers
from Healthcare.models import HealthWorker


class HealthWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthWorker
        fields = ("__all__")