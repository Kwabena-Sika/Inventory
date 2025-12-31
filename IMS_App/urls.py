from django.urls import path
from . import views

app_name = 'IMS_App'

urlpatterns = [
  path('', views.homepage, name='homepage'),
  path('add_product/', views.Add_Product, name='Add_Product'),
  path('product_list/', views.Product_list, name='Product_list'),
  path('edit_product/<int:product_id>/',views.Edit_Product, name='Edit_Product'),
  path('delete_product/<int:product_id>/', views.Delete_Product, name='Delete_Product')
]
