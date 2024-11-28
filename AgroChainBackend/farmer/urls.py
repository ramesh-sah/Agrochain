from django.urls import path
from farmer.views import FarmerLoginView, FarmerRegistrationView


urlpatterns = [
    path('register/',FarmerRegistrationView.as_view(),name='farmer_register'),
    path('login/',FarmerLoginView.as_view(),name='login_register'),
    
]
