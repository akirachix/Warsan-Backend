from rest_framework import serializers
from Immunization_Record.models import Immunization_Record



class Immunization_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model =Immunization_Record
        fields='__all__'