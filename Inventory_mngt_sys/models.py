from email.policy import default
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models


class Stock(models.Model):
    category = models.CharField(max_length=50 , blank=True , null=True)
    item_name = models.CharField(max_length=50 , blank=True , null=True)
    quantity = models.IntegerField(default='0' , blank=True , null=True)
    recieved_quantity = models.IntegerField(default='0' , blank=True , null=True)
    recieved_by = models.CharField(max_length=50 , blank=True , null=True)
    issued_quantity = models.IntegerField(default='0' , blank=True , null=True)
    issued_by = models.CharField(max_length=50 , blank=True , null=True)
    phone_number = models.CharField(max_length=15 , blank=True , null=True)
    reorder_level = models.IntegerField(default='0' , blank=True , null=True)
    last_updated = models.DateTimeField(auto_now_add=False , auto_now=True)
    
    def __str__(self):
        return self.issued_quantity + self.quantity
    
    

