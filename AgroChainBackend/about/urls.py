from django.urls import path
from .views import AboutAPIView, AdminAboutAPIView

urlpatterns = [
    path('about/', AboutAPIView.as_view(), name='about-getAll'),
    path('about/<int:pk>', AboutAPIView.as_view(), name='about-getSpecific'),
    
    path('admin-about/', AdminAboutAPIView.as_view(), name='admin-about-create'),
    path('admin-about/<int:pk>', AdminAboutAPIView.as_view(), name='admin-about-update-delete'),
]
