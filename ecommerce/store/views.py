from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
import datetime
from .models import * 




def home(request):

	return render(request, 'store/index.html')
	

def store(request):

	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def login(request):
    return render(request, 'store/login.html')


def signup(request):
	if  request.method =='GET':
		return render(request, 'store/signup.html')
	else:
		first_name = request.POST.get('firstname')
		email = request.POST.get('email')
		password =request.POST.get('password')
		customer = Customer(first_name=first_name,email=email, password=password)
		values = {
            'firstname': first_name,
            'email': email,
        }
		err_msg = None
		if not first_name:
			 err_msg = "First Name Required."
		elif len(first_name) < 3:
			err_msg = "First Name must be 3 characters long."
		elif not phone:
			err_msg = "Phone is Required."
		elif len(phone) < 10:
			err_msg = "Phone Number must be 10 characters long."
		elif not email:
			err_msg = "Email is Required."
		if not err_msg:
			customer.save()
			return HttpResponse("<h3>Signup Successful</h3>")
		else:
			return render(request, 'store/signup.html', {'error_msg': err_msg,'values': values})
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)