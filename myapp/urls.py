from django.urls import path
from .views import home,tentang,layanan,kontak
urlpatterns = [
    path('', home, name='home.html'),
    path('tentang', tentang, name='tentang.html'),
    path('layanan', layanan,name='layanan.html'),
    path('kontak',kontak,name='kontak.html'),
]