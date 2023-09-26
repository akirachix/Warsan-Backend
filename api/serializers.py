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
    
    class Meta:
        model = Healthworker
        fields = ('id', 'username', 'email', 'first_name', 'last_name','location', 'hospital')

class Immunization_RecordSerializer(serializers.ModelSerializer):
    child_name = serializers.ReadOnlyField(source='child.first_name')  
    vaccine_name = serializers.ReadOnlyField(source='vaccine.name')
   
    class Meta:
        model =Immunization_Record
        fields = ['id', 'date_of_administration', 'next_date_of_administration', 'child_name', 'vaccine_name']

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vaccine
        fields=("__all__")
    
class GuardianSerializer(serializers.ModelSerializer):
     child_name = serializers.ReadOnlyField(source='child.first_name')  
     class Meta:
        model = Guardian
        fields = ['id','first_name','last_name','phone_number','status','location','child_name']

class ChildSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Child
        fields = '__all__'

       