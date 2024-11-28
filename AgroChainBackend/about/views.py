from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import About
from .serializers import AboutSerializer

class AboutAPIView(APIView):
    """
    APIView to handle About app data.
    """

    def get(self, request, *args, **kwargs):
        """
        Retrieve all about information.
        """
        about_entries = About.objects.all()
        serializer = AboutSerializer(about_entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Add new about information. Accessible to all for simplicity.
        """
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
