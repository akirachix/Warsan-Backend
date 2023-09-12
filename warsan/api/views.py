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
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif operation == 'patch':
                serializer = LocationSerializer(location, data=request.data, partial=True)
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