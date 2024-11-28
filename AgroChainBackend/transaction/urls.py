from django.urls import path
from .views import TransactionAPIView

urlpatterns = [
    path('transactions/', TransactionAPIView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionAPIView.as_view(), name='transaction-detail'),
]
