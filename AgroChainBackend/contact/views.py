from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAdminUser

class ContactAPIView(APIView):
    """
    APIView for handling contact submissions.
    """

    def get(self, request, *args, **kwargs):
        """
        Retrieve all contact inquiries. Typically, this is for admin purposes.
        """
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Handle the submission of a new contact form.
        Accessible to anyone.
        """
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer

class AdminContactAPIView(APIView):
    permission_classes=[IsAdminUser]
    """
    APIView for handling contact submissions, accessible for admin purposes.
    """

    def get(self, request, *args, **kwargs):
        """
        Retrieve all contact inquiries or a specific contact inquiry by ID (primary key).
        """
        # Check if a 'pk' is provided in the URL
        pk = kwargs.get('pk', None)

        if pk:
            # If 'pk' is provided, retrieve the specific contact inquiry
            try:
                contact = Contact.objects.get(pk=pk)  # Retrieve specific contact inquiry by ID
            except Contact.DoesNotExist:
                return Response({"detail": "Contact not found."}, status=status.HTTP_404_NOT_FOUND)

            # Serialize the specific contact and return the response
            serializer = ContactSerializer(contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # If 'pk' is not provided, retrieve all contact inquiries
            contacts = Contact.objects.all()  # Retrieve all contact inquiries
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    def patch(self, request, pk, *args, **kwargs):
        """
        Partially update a contact inquiry by ID (primary key).
        """
        try:
            contact = Contact.objects.get(pk=pk)  # Retrieve specific contact inquiry by ID
        except Contact.DoesNotExist:
            return Response({"detail": "Contact not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save the updated contact inquiry
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)