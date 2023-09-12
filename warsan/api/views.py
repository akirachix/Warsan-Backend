# views.py
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from Healthcare.models import HealthWorker
from .serializers import HealthWorkerSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

class HealthWorkerListView(generics.ListCreateAPIView):
    queryset = HealthWorker.objects.all()
    serializer_class = HealthWorkerSerializer

    def list(self, request, *args, **kwargs):
        # Handle the GET request to list all HealthWorker objects
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Handle the POST request to create a new HealthWorker object
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HealthWorkerSearchView(generics.ListAPIView):
    queryset = HealthWorker.objects.all()
    serializer_class = HealthWorkerSerializer

    def get(self, request, *args, **kwargs):
        # Handle the GET request to search HealthWorker objects
        search_term = request.query_params.get('search')
        queryset = self.get_queryset()

        if search_term:
            queryset = queryset.filter(
                Q(first_name__icontains=search_term) |
                Q(middle_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(hospital__icontains=search_term)
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HealthWorkerFilterView(generics.ListAPIView):
    queryset = HealthWorker.objects.all()
    serializer_class = HealthWorkerSerializer

    def get(self, request, *args, **kwargs):
        # Handle the GET request to filter HealthWorker objects
        hospital = request.query_params.get('hospital')
        queryset = self.get_queryset()

        if hospital:
            queryset = queryset.filter(hospital__icontains=hospital)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HealthWorkerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthWorker.objects.all()
    serializer_class = HealthWorkerSerializer

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=kwargs.get('pk'))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=kwargs.get('pk'))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=kwargs.get('pk'))
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            phone_number = serializer.validated_data.get('phone_number')
            if HealthWorker.objects.exclude(pk=instance.pk).filter(phone_number=phone_number).exists():
                return Response({'phone_number': ['Phone number already exists for another health worker.']}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view
from Registrations.models import UserProfile
from .serializers import UserProfileSerializer, UserRegistrationSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({'message': 'User logged in successfully.'})
    return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'message': 'User logged out successfully.'})

@api_view(['GET'])
def list_users(request):
    # Retrieve all user profiles
    user_profiles = UserProfile.objects.all()

    # Serialize the user profiles
    serializer = UserProfileSerializer(user_profiles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET'])
def get_user_list(request):
    # Retrieve all user profiles
    user_profiles = UserProfile.objects.all()

    # Serialize the user profiles
    serializer = UserProfileSerializer(user_profiles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def edit_user(request, user_id):
    try:
        user_profile = UserProfile.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserRegistrationSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user_profile = UserProfile.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user_profile.delete()
        logout(request)
        return Response({'message': 'User deleted successfully.'})
