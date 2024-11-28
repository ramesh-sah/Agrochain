from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TermsAndConditions
from .serializers import TermsAndConditionsSerializer

class TermsAndConditionsAPIView(APIView):
    
    
    """
    List all Terms and Conditions or create a new Terms and Conditions
    """
    def get(self, request, *args, **kwargs):
        terms = TermsAndConditions.objects.all()
        serializer = TermsAndConditionsSerializer(terms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TermsAndConditionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    """
    Retrieve, update or delete a specific Terms and Conditions.
    """
    def get_object(self, pk):
        try:
            return TermsAndConditions.objects.get(pk=pk)
        except TermsAndConditions.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        terms = self.get_object(pk)
        if not terms:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TermsAndConditionsSerializer(terms)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        terms = self.get_object(pk)
        if not terms:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TermsAndConditionsSerializer(terms, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        terms = self.get_object(pk)
        if not terms:
            return Response(status=status.HTTP_404_NOT_FOUND)
        terms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
