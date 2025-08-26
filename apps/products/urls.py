from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('',views.cart_view,name='card'),
    path('category/',views.category_view,name='category'),
    path('checkout/',views.checkout_view,name='category'),
    path('product-detail/',views.product_view,name='detail'),
    path('wishlist/',views.wishlist_view,name='wishlist'),
]