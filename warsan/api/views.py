from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework import status
from rest_framework.views import APIView
from Immunization_Record.models import Immunization_Record
from .serializer import Immunization_RecordSerializer

class Immunization_recordView(APIView):
    def get(self, request):
        immunization_record=Immunization_Record.objects.all()
        serializers=Immunization_RecordSerializer (immunization_record, many=True)
        return Response(serializers.data)