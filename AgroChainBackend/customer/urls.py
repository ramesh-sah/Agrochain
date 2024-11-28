from django.urls import path
from .views  import CustomerLoginView, CustomerRegistrationView

urlpatterns = [
    path('register/',CustomerRegistrationView.as_view(),name='customer_register'),
    path('login/',CustomerLoginView.as_view(),name='login_register'),
    
]
