from django.contrib import admin 
from django.urls import path 
from . import views
from .views import MenuItemView, SingleMenuItemView, index
  
urlpatterns = [ 
   path('menu/items/', MenuItemView.as_view(), name='menu-list-create'),
   path('menu/items/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
   path('', views.index, name='index'),
]