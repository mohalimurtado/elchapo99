from django.urls import path
from .views import beranda,tentang,layanan,kontak,hubungi

urlpatterns = [
    path('', beranda, name='beranda'),
    path('tentang', tentang, name='tentang'),
    path('layanan',layanan,name='layanan'),
    path('kontak',kontak,name='kontak'),
    path('hubungi',hubungi,name='hubungi'),
]
