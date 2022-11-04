
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home ) ,
    path('list_items/', views.list_items , name = 'list_item' ) ,
    path('add_item/', views.add_item , name = 'add_item') ,
    path('update_item/<str:pk>/', views.update_item, name="update_item") ,
]