from dataclasses import fields
from unicodedata import category
from django import forms

from Inventory_mngt_sys.models import Stock



class StockCreateForm(forms.ModelForm):
    #category = forms.CharField(required=True, max_length=50)
    #item_name = forms.CharField(required=True, max_length=50)
    
    class Meta:
        model = Stock
        fields = [ 'category', 'item_name' , 'quantity']
        
    def clean_category(self):
        category = self.cleaned_data.get("category")
        
        if not category:
            raise forms.ValidationError("This field is required") 
        
        return category
	            
    
    def clean_item_name(self):
        item_name = self.cleaned_data.get("item_name") 
        if not item_name:
            raise forms.ValidationError("Please fill in this field")
        for instance in Stock.objects.all():
            if instance.item_name == item_name:
                raise forms.ValidationError(str(item_name) + ' is already created')
        return item_name  
      
class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name' , 'quantity']    
 
    
class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [ 'category', 'item_name']     
    
   

