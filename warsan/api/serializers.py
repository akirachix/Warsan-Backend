from rest_framework import serializers
from registration.models import CustomUser, Healthworker

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class HealthworkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healthworker
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'location', 'created_by')

