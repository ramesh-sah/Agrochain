from django.db import models
from distributor.models import Distributor
from retailer.models import Retailer
from product.models import Product

# Define choices for contract types
CONTRACT_TYPE_CHOICES = [
    ('SALE', 'Sale'),
    ('LEASE', 'Lease'),
    ('SERVICE', 'Service Agreement'),
    ('PARTNERSHIP', 'Partnership Agreement'),
    ('PURCHASE_ORDER', 'Purchase Order'),
    ('SUPPLY_AGREEMENT', 'Supply Agreement'),
    ('DISTRIBUTION', 'Distribution Agreement'),
    ('CONTRACT_FARMING', 'Contract Farming'),
    ('FRANCHISE', 'Franchise Agreement'),
    ('JOINT_VENTURE', 'Joint Venture Agreement'),
    ('CONSULTING', 'Consulting Agreement'),
    ('COOPERATIVE', 'Cooperative Agreement'),
    ('MEMORANDUM', 'Memorandum of Understanding'),
    ('OTHER', 'Other'),
]
# Create your models here.
class SmartContract(models.Model):
   
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE_CHOICES)  # Updated max_length for efficiency
    initiator = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name='initiated_contracts')
    receiver = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name='received_contracts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  # Active or inactive
    terms_and_conditions = models.TextField()
    payment_terms = models.TextField()
    valid_until = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)