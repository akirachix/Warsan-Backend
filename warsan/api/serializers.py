from rest_framework import serializers
from ChildGuardianManager.models import Guardian
from ChildGuardianManager.models import Child

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'
