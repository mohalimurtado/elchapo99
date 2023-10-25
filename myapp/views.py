from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def beranda(request):
    template = loader.get_template('beranda.html')
    return HttpResponse(template.render())

def tentang(request):
    return render(request, 'tentang.html')

def layanan(request):
    return render(request, 'layanan.html')


def kontak(request):
    return render(request, 'kontak.html')

def hubungi(request):
    return render(request, 'hubungi.html')


