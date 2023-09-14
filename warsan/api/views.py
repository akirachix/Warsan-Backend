# child/api/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from child.models import Child, Guardian
from .serializers import ChildSerializer, GuardianSerializer

class GuardianList(APIView):
    def get(self, request, format=None):
        guardians = Guardian.objects.all()
        serializer = GuardianSerializer(guardians, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GuardianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GuardianDetail(APIView):
    def handle_guardian_operations(self, request, pk, operation):
        try:
            guardian = Guardian.objects.get(pk=pk)
            if operation == 'get':
                serializer = GuardianSerializer(guardian)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif operation == 'put':
                serializer = GuardianSerializer(guardian, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif operation == 'delete':
                guardian.delete()
                return Response("Guardian deleted", status=status.HTTP_204_NO_CONTENT)
        except Guardian.DoesNotExist:
            return Response("Guardian not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        return self.handle_guardian_operations(request, pk, 'get')

    def put(self, request, pk, format=None):
        return self.handle_guardian_operations(request, pk, 'put')

    def delete(self, request, pk, format=None):
        return self.handle_guardian_operations(request, pk, 'delete')

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
    def handle_child_operations(self, request, pk, operation):
        try:
            child = Child.objects.get(pk=pk)
            if operation == 'get':
                serializer = ChildSerializer(child)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif operation == 'put':
                serializer = ChildSerializer(child, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif operation == 'delete':
                child.delete()
                return Response("Child deleted", status=status.HTTP_204_NO_CONTENT)
        except Child.DoesNotExist:
            return Response("Child not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        return self.handle_child_operations(request, pk, 'get')

    def put(self, request, pk, format=None):
        return self.handle_child_operations(request, pk, 'put')

    def delete(self, request, pk, format=None):
        return self.handle_child_operations(request, pk, 'delete')