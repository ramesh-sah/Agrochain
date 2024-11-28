from django.urls import path

from retailer.views import RetailerLoginView, RetailerRegistrationView


urlpatterns = [
    path('register/',RetailerRegistrationView.as_view(),name='retailer_register'),
    path('login/',RetailerLoginView.as_view(),name='retailer_login')
    
]
