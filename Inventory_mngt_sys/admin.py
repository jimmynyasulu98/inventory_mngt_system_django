from django.contrib import admin
from .forms import StockCreateForm
from .models import Stock


admin.site.register(Stock)

