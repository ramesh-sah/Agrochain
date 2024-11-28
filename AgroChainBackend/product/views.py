from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from agrochain.permission import IsFarmer
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsFarmer]

    def get_queryset(self):
        # Only allow farmers to see their own products
        return self.queryset.filter(farmer=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(farmer=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        if product.farmer != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.farmer != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)