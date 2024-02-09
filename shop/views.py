from django.shortcuts import render
from shop.models import Product, Order
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


# Detail Page
def detail(request, id):
	product_obj = Product.objects.get(id=id)
	return render(request, 'shop/detail.html', {'product_obj' : product_obj})


# Checkout Page
def checkout(request):
	if request.method == "POST":
		items = request.POST.get('items', '')
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		address = request.POST.get('address', '')
		city = request.POST.get('city', '')
		state = request.POST.get('state', '')
		zipcode = request.POST.get('zipcode', '')
		total = request.POST.get('total', '')

		# Create Order and add it to the database
		order = Order(items=items,
						name=name,
						email=email,
						address=address,
						city=city,
						state=state,
						zipcode=zipcode,
						total=total)
		order.save()

	return render(request, 'shop/checkout.html', {})
