from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers
from ChildGuardianManager.models import Guardian
from ChildGuardianManager .models import Child
from .serializers import GuardianSerializer, ChildSerializer

class GuardianListView(APIView):
    def get (self, request):

        guardian = Guardian.objects.all()
        serializer= GuardianSerializer(guardian,many = True)
        return Response (serializer.data)
    
    def post (self, request):
        serializer = GuardianSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    

class GuardianDetailView(APIView):
    def get_object(self, pk):
        try:
            return Guardian.objects.get(pk=pk)
        except Guardian.DoesNotExist:
            raise HTTP404

    def get (self, request, pk):
        Guardian= self.get_object(pk)    
        serializer= GuardianSerializer(Guardian)
        return Response(serializer.data)
    
    def put (self, request, pk):
        Guardian= self.get_object(pk)
        serializer=GuardianSerializer(Guardian,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, pk):
        Guardian= self.get_object(pk)
        Guardian.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChildListView(APIView):
    def get (self, request):

        guardian = Child.objects.all()
        serializer= ChildSerializer(guardian,many = True)
        return Response (serializer.data)
    
    def post (self, request):
        serializer = ChildSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    

class ChildDetailView(APIView):
    def get_object(self, pk):
        try:
            return Child.objects.get(pk=pk)
        except Child.DoesNotExist:
            raise HTTP404

    def get (self, request, pk):
        Child= self.get_object(pk)    
        serializer= ChildSerializer(Guardian)
        return Response(serializer.data)
    
    def put (self, request, pk):
        Child= self.get_object(pk)
        serializer= ChildSerializer(Guardian,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, pk):
        Child= self.get_object(pk)
        Child.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

