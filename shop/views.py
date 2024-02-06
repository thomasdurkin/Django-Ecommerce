from django.shortcuts import render
from shop.models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
	product_objs = Product.objects.all()

	# Text field from index.html for search bar
	item_name = request.GET.get('item_name')
	if item_name != '' and item_name is not None:
		product_objs = product_objs.filter(title__icontains = item_name)

	# Pagination
	paginator = Paginator(product_objs, 4)
	page = request.GET.get('page')
	product_objs = paginator.get_page(page)

	return render(request, 'shop/index.html', {'product_objs' : product_objs})
