from django.contrib import admin 
from django.urls import path 
from . import views
from .views import MenuItemView, SingleMenuItemView
#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
   path('menu/items/', MenuItemView.as_view(), name='menu-list-create'),
   path('menu/items/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
   path('', views.index, name='index'),
   path('api-token-auth/', obtain_auth_token),
]