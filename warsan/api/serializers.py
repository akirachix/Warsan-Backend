from rest_framework import serializers
from Healthcare.models import HealthWorker


class HealthWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthWorker
        fields = ("__all__")


from django.contrib.auth.models import User
from Registrations.models import UserProfile
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

