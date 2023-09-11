

# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from Healthcare.models import HealthWorker
from .serializers import HealthWorkerSerializer

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
                Q(location__icontains=search_term) |
                Q(hospital__icontains=search_term)
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HealthWorkerFilterView(generics.ListAPIView):
    queryset = HealthWorker.objects.all()
    serializer_class = HealthWorkerSerializer

    def get(self, request, *args, **kwargs):
        # Handle the GET request to filter HealthWorker objects
        location = request.query_params.get('location')
        hospital = request.query_params.get('hospital')
        queryset = self.get_queryset()

        if location:
            queryset = queryset.filter(location__icontains=location)

        if hospital:
            queryset = queryset.filter(hospital__icontains=hospital)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HealthWorkerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthWorker.objects.all()
    serializer_class = HealthWorkerSerializer

    def get(self, request, *args, **kwargs):
        # Handle the GET request to retrieve a single HealthWorker object
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        # Handle the DELETE request to delete a HealthWorker object
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            # Check if the phone number already exists for another health worker
            phone_number = serializer.validated_data.get('phone_number')
            if HealthWorker.objects.exclude(pk=instance.pk).filter(phone_number=phone_number).exists():
                return Response({'phone_number': ['Phone number already exists for another health worker.']}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
