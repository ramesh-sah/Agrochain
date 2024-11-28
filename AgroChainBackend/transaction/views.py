from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer


class CustomerTransactionAPIView(APIView):
    """
    APIView for handling CRUD operations for Transaction.
    """

    def get(self, request, pk=None, *args, **kwargs):
        """
        Retrieve all transactions or a single transaction by ID.
        """
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        if pk:
            try:
                transaction = Transaction.objects.get(pk=pk)
                # Ensure user has access
                if user.user_type == 'customer' and transaction.buyer != user:
                    return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
                elif user.user_type != 'customer' and transaction.initiator != user:
                    return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

                serializer = TransactionSerializer(transaction)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Filter transactions based on user type
            if user.user_type == 'customer':
                transactions = Transaction.objects.filter(buyer=user)
            else:
                transactions = Transaction.objects.filter(initiator=user)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a new transaction.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(initiator=request.user)  # Assuming `initiator` is the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        """
        Update an entire transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        """
        Partially update a transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        """
        Delete a transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        transaction.delete()
        return Response({"detail": "Transaction deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



class DistributorTransactionAPIView(APIView):
    """
    APIView for handling CRUD operations for Transaction.
    """

    def get(self, request, pk=None, *args, **kwargs):
        """
        Retrieve all transactions or a single transaction by ID.
        """
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        if pk:
            try:
                transaction = Transaction.objects.get(pk=pk)
                # Ensure user has access
                if user.user_type == 'customer' and transaction.buyer != user:
                    return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
                elif user.user_type != 'customer' and transaction.initiator != user:
                    return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

                serializer = TransactionSerializer(transaction)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Filter transactions based on user type
            if user.user_type == 'customer':
                transactions = Transaction.objects.filter(buyer=user)
            else:
                transactions = Transaction.objects.filter(initiator=user)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a new transaction.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(initiator=request.user)  # Assuming `initiator` is the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        """
        Update an entire transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        """
        Partially update a transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        """
        Delete a transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        transaction.delete()
        return Response({"detail": "Transaction deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    
    

class RetailerTransactionAPIView(APIView):
    """
    APIView for handling CRUD operations for Transaction.
    """

    def get(self, request, pk=None, *args, **kwargs):
        """
        Retrieve all transactions or a single transaction by ID.
        """
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        if pk:
            try:
                transaction = Transaction.objects.get(pk=pk)
                # Ensure user has access
                if user.user_type == 'customer' and transaction.buyer != user:
                    return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
                elif user.user_type != 'customer' and transaction.initiator != user:
                    return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

                serializer = TransactionSerializer(transaction)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Filter transactions based on user type
            if user.user_type == 'customer':
                transactions = Transaction.objects.filter(buyer=user)
            else:
                transactions = Transaction.objects.filter(initiator=user)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a new transaction.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(initiator=request.user)  # Assuming `initiator` is the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        """
        Update an entire transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        """
        Partially update a transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        """
        Delete a transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        transaction.delete()
        return Response({"detail": "Transaction deleted successfully."}, status=status.HTTP_204_NO_CONTENT)




class FarmerTransactionAPIView(APIView):
    """
    APIView for handling CRUD operations for Transaction.
    """

    def get(self, request, pk=None, *args, **kwargs):
        """
        Retrieve all transactions or a single transaction by ID.
        """
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        if pk:
            try:
                transaction = Transaction.objects.get(pk=pk)
                # Ensure user has access
                if user.user_type == 'customer' and transaction.buyer != user:
                    return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
                elif user.user_type != 'customer' and transaction.initiator != user:
                    return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

                serializer = TransactionSerializer(transaction)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Filter transactions based on user type
            if user.user_type == 'customer':
                transactions = Transaction.objects.filter(buyer=user)
            else:
                transactions = Transaction.objects.filter(initiator=user)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a new transaction.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(initiator=request.user)  # Assuming `initiator` is the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        """
        Update an entire transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        """
        Partially update a transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        """
        Delete a transaction by ID.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != transaction.initiator:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        transaction.delete()
        return Response({"detail": "Transaction deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
