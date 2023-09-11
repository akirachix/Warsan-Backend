from rest_framework import serializers
from Healthcare.models import HealthWorker
from Registration.models import Registrations
from django.contrib.auth.models import User


class HealthWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthWorker
        fields = ("__all__")


