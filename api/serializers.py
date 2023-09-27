from rest_framework import serializers
from location.models import Location
from Immunization_Record.models import Immunization_Record
from vaccine.models import Vaccine
from child.models import Child, Guardian

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
from registration.models import CustomUser, Healthworker

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username','password', 'email', 'first_name', 'last_name')

class HealthworkerSerializer(serializers.ModelSerializer):
    location_name=serializers.ReadOnlyField(source='location.region')
    class Meta:
        model = Healthworker
        fields = ('id', 'username', 'email', 'first_name', 'last_name','location_name', 'hospital')

class Immunization_RecordSerializer(serializers.ModelSerializer):
    child_name = serializers.ReadOnlyField(source='child.first_name')  
    vaccine_name = serializers.ReadOnlyField(source='vaccine.name')
    guardian_name = serializers.ReadOnlyField(source='guardian.first_name')  
    guardian_number=serializers.ReadOnlyField(source='guardian.phone_number')
    guardian_location=serializers.ReadOnlyField(source='guardian.location')
    class Meta:
        model =Immunization_Record
        fields = ['id','child_name','vaccine_name','guardian_name','guardian_number','guardian_location','date_of_administration', 'next_date_of_administration', 'child_name', 'vaccine_name']

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vaccine
        fields=("__all__")
    
class GuardianSerializer(serializers.ModelSerializer):
   
     class Meta:
        model = Guardian
        fields = ['id','first_name','last_name','phone_number','status','location','child_name']

class ChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Child
        fields = ['id','first_name','last_name','date_of_birth','gender','status','guardian_name','guardian_number']

       