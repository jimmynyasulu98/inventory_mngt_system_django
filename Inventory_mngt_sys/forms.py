from dataclasses import fields
from django import forms

from Inventory_mngt_sys.models import Stock



class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item_name' , 'quantity']
