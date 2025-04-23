from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path('', product_list),  # GET /api/product/
    path('<int:pk>/', product_detail),  # GET /api/product/1/
]
