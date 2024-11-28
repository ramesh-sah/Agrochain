from django.urls import path
from .views import SmartContractAPIView

urlpatterns = [
    path('smart-contracts/', SmartContractAPIView.as_view(), name='smart-contract-list-create'),
    path('smart-contracts/<int:pk>/', SmartContractAPIView.as_view(), name='smart-contract-detail'),
]
