from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers
from vaccine.models import Vaccine
from .serializers import VaccineSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class VaccineListView(APIView):
    @swagger_auto_schema(
        operation_description="Get a list of all vaccines",
        responses={200: VaccineSerializer(many=True)},
    )
    def get(self, request):
        vaccine = Vaccine.objects.all()
        serializer = VaccineSerializer(vaccine, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new vaccine",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'manufacturer': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={201: VaccineSerializer()},
    )
    def post(self, request):
        serializer = VaccineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
