
from django.contrib import admin
from django.urls import path

from app.views import index, product_detail, category_product, categories_list, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('category/<int:category_id>/', category_product, name='category_detail'),
    path('categories_list/', categories_list, name='categories_list'),
    path('search/', search, name='search'),
]
