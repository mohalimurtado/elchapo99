from django.urls import path
from .views import home,produk,login,pesan,keranjang,checkout
urlpatterns = [
    path('', home, name='home.html'),
    path('produk', produk,name='produk.html'),
    path('login',login,name='login.html'),
    path('pesan',pesan,name='pesan.html'),
    path('keranjang',keranjang,name='keranjang.html'),
    path('checkout',checkout,name='checkout.html'),
]