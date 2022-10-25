import imp
from django.shortcuts import render
from . models import Stock
from . forms import StockCreateForm

def home(request):
    
    return render(request , "home.html")

def list_items(request):
    stock = Stock.objects.all()
    context = {
        "stock" : stock 
    }
    return render(request , "list_items.html", context)

def add_item(request):
    form = StockCreateForm()
    if request.method == 'POST':
        form = StockCreateForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        "form" : form
    }        
    return render(request , 'add_item.html', context )       

def edit_item(request):
    
    pass

def delete_item(request):
    
    pass