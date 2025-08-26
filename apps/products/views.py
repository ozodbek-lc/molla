from django.shortcuts import render

def cart_view(request):
    return render(request,'cart.html')

def category_view(request):
    return render(request,'category.html')

def checkout_view(request):
    return render(request,'checkout.html')

def product_view(request):
    return render(request,'product-detail.html')

def wishlist_view(request):
    return render(request,'wishlist.html')