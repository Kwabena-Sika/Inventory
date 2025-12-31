from django.shortcuts import render,redirect
from . forms import ProductForm
from .models import Product
# Create your views here.
# CRUD- Create, Read, Update, Delete

# Home View
def homepage(request):
  return render(request, 'IMS_App/home.html')

# Create
def Add_Product(request):
  if request.method != "POST":
    form = ProductForm()
  else:
    form = ProductForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('IMS_App:Product_list')
  
  context = {'form':form}
  return render(request, 'IMS_App/Add_Product.html', context)
# Read
def Product_list(request):
  products = Product.objects.all()
  context = {'products':products}
  return render(request, 'IMS_App/product_list.html', context)

# Update 
def Edit_Product(request, product_id):
  product = Product.objects.get(product_id=product_id)
  if request.method != "POST":
    form = ProductForm(instance=product)
  else:
    form = ProductForm(instance=product, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('IMS_App:Product_list')
  context = {'form':form, 'product':product}
  return render(request, 'IMS_App/Edit_Product.html', context)

# Delete
def Delete_Product(request, product_id):
  product = Product.objects.get(product_id = product_id)
  if request.method == 'POST':
      product.delete()
      return redirect('IMS_App:Product_list')
  context = {'product':product}
  return render(request, 'IMS_App/confirm_delete.html', context)
