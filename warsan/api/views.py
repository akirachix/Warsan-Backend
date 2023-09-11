from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers
from vaccine.models import Vaccine
from .serializers import VaccineSerializer

class VaccineListView(APIView):
    def get(self, request):
        vaccine=Vaccine.objects.all()
        serializer=VaccineSerializer(vaccine, many = True)
        return Response(serializer.data)
    
    def post(self,request):
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

    def get(self, request, pk):
        try:
            vaccine = self.get_object(pk)
            serializer = VaccineSerializer(vaccine)
            return Response(serializer.data)
        except Http404:
             return Response("Vaccine not found", status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk):
        try:
            vaccine = self.get_object(pk)
            serializer = VaccineSerializer(vaccine, data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
           return Response("Vaccine not found", status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk):
        try:
            vaccine = self.get_object(pk)
            vaccine.delete()
            return Response("Vaccine Deleted", status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response("Vaccine not found", status=status.HTTP_404_NOT_FOUND)






