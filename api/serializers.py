from rest_framework import serializers
from location.models import Location
from Immunization_Record.models import Immunization_Record
from vaccine.models import Vaccine
from child.models import Child, Guardian
from registration.models import CustomUser, Healthworker
from .child_serializers import ChildSerializer  # Import ChildSerializer from the child_serializers module

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

class HealthworkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healthworker
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'hospital', 'phone_number']

class GuardianSerializer(serializers.ModelSerializer):
    location_name = serializers.ReadOnlyField(source='location.region')
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), required=True)
    children = ChildSerializer(many=True, read_only=True)  # Include related children

    class Meta:
        model = Guardian
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'status', 'location_name', 'location', 'children']


class Immunization_RecordSerializer(serializers.ModelSerializer):
    child_first_name = serializers.ReadOnlyField(source='child.first_name')
    child_last_name = serializers.ReadOnlyField(source='child.last_name')
    child_date_of_birth = serializers.ReadOnlyField(source='child.date_of_birth')
    child_location = serializers.ReadOnlyField(source='child.location.region')
    child_phone_number = serializers.SerializerMethodField()
    vaccines = serializers.SerializerMethodField()
    guardian_name = serializers.ReadOnlyField(source='guardian.first_name')

    def get_child_phone_number(self, obj):
        return str(obj.child.phone_number)

    def get_vaccines(self, obj):
        return [{'id': vaccine.id, 'vaccine_choice': vaccine.vaccine_choice} for vaccine in obj.vaccine.all()]

    class Meta:
        model = Immunization_Record
        fields = [
            'id', 'child_first_name', 'child_last_name', 'guardian_name', 'child_date_of_birth',
            'child_location', 'child_phone_number', 'vaccines',
            'date_of_administration', 'next_date_of_administration'
        ]

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'
