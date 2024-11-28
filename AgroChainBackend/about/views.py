from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import About
from .serializers import AboutSerializer
from rest_framework.permissions import IsAdminUser

class AboutAPIView(APIView):
    
    
    """
    APIView to handle About app data.
    """

    
    def get_object(self):
        # Assuming only one About information exists in the database
        try:
            return About.objects.all().first()
        except About.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        about = self.get_object()
        if about:
            serializer = AboutSerializer(about)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "About information not found."}, status=status.HTTP_404_NOT_FOUND)




class AdminAboutAPIView(APIView):
    
    
    """
    APIView to handle About app data.
    """
    permission_classes=[IsAdminUser]

    def get_object(self):
        # Assuming only one About information exists in the database
        try:
            return About.objects.all().first()
        except About.DoesNotExist:
            return None

    
    def post(self, request, *args, **kwargs):
        """
        Add new About information. Accessible to all.
        """
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        Update About information. Accessible to all.
        """
        about = self.get_object()
        if not about:
            return Response({"detail": "About information not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        """
        Partially update About information. Accessible to all.
        """
        about = self.get_object()
        if not about:
            return Response({"detail": "About information not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Delete About information. Accessible to all.
        """
        about = self.get_object()
        if not about:
            return Response({"detail": "About information not found."}, status=status.HTTP_404_NOT_FOUND)

        about.delete()
