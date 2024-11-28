from django.urls import path
from .views import TermsAndConditionsAPIView

urlpatterns = [
    # List and create Terms and Conditions
    path('terms/', TermsAndConditionsAPIView.as_view(), name='terms-list-create'),
    
    # Retrieve, update, or delete a specific Terms and Conditions by ID
    path('terms/<int:pk>/', TermsAndConditionsAPIView.as_view(), name='terms-detail'),
]
