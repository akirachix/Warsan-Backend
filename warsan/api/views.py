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
    
    def post(self, request):
        serializer = Immunization_RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   

    def put(self, request, pk, format=None):
        immunization = Immunization_Record.objects.get(pk)
        serializer = Immunization_RecordSerializer(immunization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, pk, format=None):
        immunization= self.get_object(pk)
        immunization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
