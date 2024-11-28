from django.urls import path
from .views import ContactAPIView,AdminContactAPIView

urlpatterns = [
    path('contact/', ContactAPIView.as_view(), name='contact-create'),
    path('admin-contact/', ContactAPIView.as_view(), name='admin-getAll'),
    path('admin-contact/<int:pk>', ContactAPIView.as_view(), name='admin-contact-getSpecific-update'),
]
