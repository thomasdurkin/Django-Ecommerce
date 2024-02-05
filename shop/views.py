from django.shortcuts import render
from shop.models import Product

# Create your views here.
def index(request):
	product_objs = Product.objects.all()
	return render(request, 'shop/index.html', {'product_objs' : product_objs})
