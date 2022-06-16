from operator import imod
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list),
    path('products/<int:pk>/', views.product_detail),
]