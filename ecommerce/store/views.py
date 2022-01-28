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
		phone = request.POST.get('phone')
		last_name = request.POST.get('lastname')
		password =request.POST.get('password')
		customer = Customer(first_name=first_name,last_name=last_name,email=email,phone=phone, password=password)

		values={
			'first_name': first_name ,
			'last_name': last_name,
			'email':email,
			'phone':phone,

		}
		err_msg = None
		if not first_name:
			err_msg = "First Name Required."
		elif len(first_name) < 3:
			err_msg = "First Name must be 3 characters long."
		elif not last_name:
			err_msg = "Last Name Required."
		elif len(last_name) < 3:
			err_msg = "Last Name must be 3 characters long."
		elif not phone:
			err_msg = "Phone is Required."
		elif len(phone) < 10:
			err_msg = "Phone Number must be 10 characters long."
		elif not email:
			err_msg = "Email is Required."
		if not err_msg:
			customer.save()
			return redirect('home')
		else:
			return render(request, 'store/signup.html', {'error_msg': err_msg,"values":values})
	    
def cart(request):
	return render(request, 'store/cart.html')

def checkout(request):
	return render(request, 'store/checkout.html')

