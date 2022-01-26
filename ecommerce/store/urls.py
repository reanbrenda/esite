from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path("",views.home, name="Home"),
	path('products/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path("login/",views.login,name="login"),
	path("signup/",views.signup,name="signup"),

]