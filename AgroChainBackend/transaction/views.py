from django.shortcuts import render

from agrochain.permission import IsCustomer, IsDistributor, IsRetailer
from rest_framework import viewsets

# Create your views here.
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsDistributor | IsRetailer | IsCustomer]
        else:
            self.permission_classes = [IsDistributor | IsRetailer | IsCustomer]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            # Handle unauthenticated users
            return self.queryset.none()

        if getattr(user, 'user_type', None) == 'customer':
            # Filter for customers
            return self.queryset.filter(buyer=user)
        else:
            # Handle other user types
            return self.queryset.filter(initiator=user)