from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator  # Import default_token_generator
from django.contrib.auth.hashers import make_password  # Import make_password
from rest_framework.authtoken.models import Token
from registration.models import CustomUser, Healthworker
from .serializers import CustomUserSerializer, HealthworkerSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin



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
@permission_classes([permissions.IsAuthenticated])
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

    if request.method == 'DELETE':
        healthworker.delete()
        return Response({'message': 'Health worker deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def healthworker_signup(request):
    serializer = HealthworkerSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hashed_password = make_password(password)  # Use make_password to hash the password
        healthworker = serializer.save(password=hashed_password)  # Save the hashed password
        
        creator_id = request.data.get('created_by')
        if creator_id:
            creator = CustomUser.objects.filter(id=creator_id).first()
            if creator:
                healthworker.created_by = creator
                healthworker.save()
        
        return Response({'message': 'Health worker registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def healthworker_logout(request):
    logout(request)
    return Response({'message': 'Health worker logged out successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def healthworker_login(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    user = Healthworker.objects.filter(phone_number=phone_number).first()
    if user is not None and user.check_password(password):
        login(request, user)
        token = default_token_generator.make_token(user)  # Use default_token_generator to create a token
        return Response({'token': token}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def ngo_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = CustomUser.objects.filter(username=username).first()  # Find the NGO user by username
    
    if user is not None and user.check_password(password):  # Check the password
        login(request, user)  # Log in the user if the password is correct
        token = default_token_generator.make_token(user) # Use
        return Response({'token':token}, status=status.HTTP_200_OK)    
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
