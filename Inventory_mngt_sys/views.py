import imp
from unicodedata import category
from django.shortcuts import redirect, render
from . models import Stock
from . forms import StockCreateForm,StockUpdateForm

def home(request):
    
    return render(request , "home.html")

def list_items(request):
    
    search = request.GET.get("search")
    stock = Stock.objects.all()
    context = {
        "stock"  : stock,
     
        }
    if request.method == 'GET':
        
        if search is not None:
            search = Stock.objects.filter(category__icontains=search) 
                
            
            context = {
            "stock"  :  search,
        
        
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

def update_item(request, pk):
    
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form  = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')
        
    context = {
		'form':form
	}
    return render(request, 'add_item.html', context)    

def delete_item(request):
    
    pass