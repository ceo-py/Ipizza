from django.shortcuts import render


# Create your views here.

def checkout(request):
    return render(request, 'checkout/checkout.html')


def cart(request):
    return render(request, 'checkout/cart.html')
