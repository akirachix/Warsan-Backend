# child/api/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from child.models import Child, Guardian
from .serializers import ChildSerializer, GuardianSerializer

@api_view(['GET', 'POST'])
def guardian_list(request):
    if request.method == 'GET':
        guardians = Guardian.objects.all()
        serializer = GuardianSerializer(guardians, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GuardianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def guardian_detail(request, pk):
    try:
        guardian = Guardian.objects.get(pk=pk)
    except Guardian.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serialize the guardian along with related children
        serializer = GuardianSerializer(guardian)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GuardianSerializer(guardian, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guardian.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChildList(APIView):
    def get(self, request, format=None):
        children = Child.objects.all()
        serializer = ChildSerializer(children, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChildDetail(APIView):
    def get_object(self, pk):
        try:
            return Child.objects.get(pk=pk)
        except Child.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        child = self.get_object(pk)
        serializer = ChildSerializer(child)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        child = self.get_object(pk)
        serializer = ChildSerializer(child, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        child = self.get_object(pk)
        child.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
