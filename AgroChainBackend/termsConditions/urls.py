from django.urls import path
from .views import AdminTermsAndConditionsAPIView, TermsAndConditionsAPIView

urlpatterns = [
   path('terms/', TermsAndConditionsAPIView.as_view(), name='terms&conditions-create-getAll'),
   path('terms/<int:pk>/', TermsAndConditionsAPIView.as_view(), name='terms&conditions-create-getSpecific'),
   
   path('admin-terms/', AdminTermsAndConditionsAPIView.as_view(), name='admin-terms&conditions-create-getAll'),
    
    # Retrieve, update, or delete a specific Terms and Conditions by ID
    path('admin-terms/<int:pk>/', AdminTermsAndConditionsAPIView.as_view(), name='admin-terms&conditions-update-delete-getSpecific'),
]
