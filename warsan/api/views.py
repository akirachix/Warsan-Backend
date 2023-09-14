from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from location.models import Location
from .serializers import LocationSerializer

# Create your views here.


 # List of all locations,create new location.
class LocationListView(APIView):
        
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

 # Retrieve, update, or delete a location by id.
class LocationDetailView(APIView):
    def perform_crud_operations(self, request, id, operation):
        try:
            location = Location.objects.get(id=id)
            if operation == 'get':
                serializer = LocationSerializer(location)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif operation == 'put':
                serializer = LocationSerializer(location, data=request.data)

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

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from registration.models import CustomUser, Healthworker
from .serializers import CustomUserSerializer, HealthworkerSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin, IsAdminOrNGO, IsHealthworker

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def ngo_signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'message': 'NGO user created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminOrNGO])
def ngo_logout(request):
    logout(request)
    return Response({'message': 'NGO user logged out successfully'}, status=status.HTTP_200_OK)

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminOrReadOnly]

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminOrReadOnly]

class HealthworkerList(generics.ListCreateAPIView):
    queryset = Healthworker.objects.all()
    serializer_class = HealthworkerSerializer
    permission_classes = [IsAdminOrReadOnly]

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrAdmin])
def healthworker_detail(request, pk):
    try:
        healthworker = Healthworker.objects.get(pk=pk)
    except Healthworker.DoesNotExist:
        return Response({'message': 'Health worker not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HealthworkerSerializer(healthworker)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = HealthworkerSerializer(healthworker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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
            elif operation == 'patch':
                serializer = LocationSerializer(location, data=request.data, partial=True)
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



    if request.method == 'DELETE':
        healthworker.delete()
        return Response({'message': 'Health worker deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAdminOrNGO])
def healthworker_signup(request):
    serializer = HealthworkerSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')  
        hashed_password = make_password(password)
        healthworker = serializer.save(password=hashed_password)

        creator_id = request.data.get('created_by')
        if creator_id:
            creator = CustomUser.objects.filter(id=creator_id).first()
            if creator:
                healthworker.created_by = creator
                healthworker.save()

        return Response({'message': 'Health worker registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminOrNGO])
def healthworker_logout(request):
    logout(request)
    return Response({'message': 'Health worker logged out successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsHealthworker])
def healthworker_login(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    user = Healthworker.objects.filter(phone_number=phone_number).first()
    print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<{user}>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if user is not None and user.check_password(password):
        login(request, user)
        token = default_token_generator.make_token(user)
        print(user)
        return Response({'token': token}, status=status.HTTP_200_OK)
    elif user is None:
        return Response({'message': 'User with this phone number does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAdminOrNGO])
def ngo_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = CustomUser.objects.filter(username=username).first()
    print(f"[[[[[[[[[[[[[[[[[[{user}==============")
    
    if user is not None and user.check_password(password):
        login(request, user)
        token = default_token_generator.make_token(user)
        return Response({'token': token}, status=status.HTTP_200_OK)    
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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
                location.delete()
                return Response("Location deleted", status=status.HTTP_204_NO_CONTENT)
        except Location.DoesNotExist:
            return Response("Location not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        return self.perform_crud_operations(request, id, 'get')

    def put(self, request, id):
        return self.perform_crud_operations(request, id, 'put')

    def patch(self, request, id):
        return self.perform_crud_operations(request, id, 'patch')

    def delete(self, request, id):
        return self.perform_crud_operations(request, id, 'delete')

 # List of all states. 
class StateListView(APIView):
    
    def get(self, request):
        states = Location.objects.values_list('state', flat=True).distinct()
        return Response(states, status=status.HTTP_200_OK)
    
#  # List of all regions.
# class RegionListView(APIView):
     
#     def get(self, request):
#         regions = Location.objects.values_list('region', flat=True).distinct()
#         return Response(regions, status=status.HTTP_200_OK)
    
    # List of all regions under a specific state.
class SpecificRegionListView(APIView):
   
    def get(self, request, state_name):
        regions = Location.objects.filter(state=state_name).values_list('region', flat=True).distinct()
        return Response(regions, status=status.HTTP_200_OK)

 
    # List of all districts under a specific region.   
class SpecificDistrictListView(APIView):
  
    def get(self, request, state_name, region_name):
        districts = Location.objects.filter(state=state_name, region=region_name).values_list('district', flat=True).distinct()
        return Response(districts, status=status.HTTP_200_OK)    
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




