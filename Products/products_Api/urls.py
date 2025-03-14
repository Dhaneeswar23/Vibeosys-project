from django.urls import path
from  .import views

urlpatterns = [
    path('API/products/add/',views.add_product,name="add_product"),
    path('API/products/<int:pid>/update/',views.update_product,name="update_product"),
    path('API/products/<int:pid>/info/',views.view_product,name="view_product"),
    path('API/products/list/',views.all_products,name="products_all"),
    
]

