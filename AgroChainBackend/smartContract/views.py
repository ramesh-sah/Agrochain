from django.shortcuts import render

from agrochain.permission import IsDistributor, IsRetailer
from rest_framework import viewsets

# Create your views here.
from .models import SmartContract
from .serializers import SmartContractSerializer


class SmartContractViewSet(viewsets.ModelViewSet):
    queryset = SmartContract.objects.all()
    serializer_class = SmartContractSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            self.permission_classes = [IsDistributor | IsRetailer]
        else:
            self.permission_classes = [IsDistributor | IsRetailer]
        return super().get_permissions()

    def get_queryset(self):
        # Allow users to see contracts they are involved in
        return self.queryset.filter(initiator=self.request.user) | self.queryset.filter(receiver=self.request.user)