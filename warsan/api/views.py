from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers
from vaccine.models import Vaccine
from .serializers import VaccineSerializer

class VaccineListView(APIView):
    def get(self, request):
        vaccines = Vaccine.objects.all()
        serializer = VaccineSerializer(vaccines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VaccineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VaccineDetailView(APIView):
    def get_object(self, pk):
        try:
            return Vaccine.objects.get(pk=pk)
        except Vaccine.DoesNotExist:
            raise Http404

    def handle_vaccine_operations(self, request, pk, operation):
        try:
            vaccine = self.get_object(pk)
            if operation == 'get':
                serializer = VaccineSerializer(vaccine)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif operation == 'put':
                serializer = VaccineSerializer(vaccine, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif operation == 'delete':
                vaccine.delete()
                return Response("Vaccine Deleted", status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response("Vaccine not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        return self.handle_vaccine_operations(request, pk, 'get')

    def put(self, request, pk):
        return self.handle_vaccine_operations(request, pk, 'put')

    def delete(self, request, pk):
        return self.handle_vaccine_operations(request, pk, 'delete')





