from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Immunization_Record.models import Immunization_Record
from .serializer import Immunization_RecordSerializer

class Immunization_recordView(APIView):
    def get(self, request):
        immunization_records = Immunization_Record.objects.all()
        serializer = Immunization_RecordSerializer(immunization_records, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Immunization_RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ImmunizationDetailView(APIView):
    def get_object(self, ):
        try:
            return Immunization_Record.objects.get(id=id)
        except Immunization_Record.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        immunization = self.get_object(id)
        serializer = Immunization_RecordSerializer(immunization)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        immunization = self.get_object(id)
        serializer = Immunization_RecordSerializer(immunization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id, format=None):
        immunization = self.get_object(id)
        immunization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

