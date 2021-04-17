from django.urls import path

from core.views import products_list, product_detail, categories_list, categories_detail

urlpatterns = [
    path('products/', products_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', categories_list),
    path('categories/<int:category_id>/', categories_detail),
]