from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('products', views.product_describe_view, name='product_add'), 
]
