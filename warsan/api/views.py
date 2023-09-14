
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
     def immunization_detail(self, request, pk, operation):
        try:
            immunization_Record = Immunization_Record.objects.get(pk=pk)
            if operation == 'get':
                serializer = Immunization_RecordSerializer(immunization_Record)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif operation == 'put':
                immunization_record = Immunization_Record.objects.get(pk=pk)
                serializer = Immunization_RecordSerializer(immunization_record, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif operation == 'delete':
                Immunization_Record.delete()
                return Response("Record deleted", status=status.HTTP_204_NO_CONTENT)
        except Immunization_Record.DoesNotExist:
            return Response("Record not found", status=status.HTTP_404_NOT_FOUND)
        
     def get(self, request, pk, format=None):
        return self.immunization_detail(request, pk, 'get')
     
     def put(self, request, pk, format=None):
        return self.immunization_detail(request, pk, 'put')
     
     def delete(self, request, pk, format=None):
        return self.immunization_detail(request, pk, 'delete')





