from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from .models import Liburuak, Autoreak

def index(request):
    autoreak = Autoreak.objects.all
    liburuak = Liburuak.objects.all
    return render(request, 'index.html', {'liburuak':liburuak , 'autoreak':autoreak})


def addlib(request):
    autoreak = Autoreak.objects.all
    return render(request, 'addlib.html', {'autoreak':autoreak})

def addliburua(request, izena):
    
    iz = request.POST["izenburua"]
    ed = request.POST["edukia"]
    au = Autoreak.objects.get(izena = izena)
    liburuberria = Liburuak(izenburua = iz, edukia=ed, noizsortua="",autorea=au)
    liburuberria.save()
    
    return HttpResponseRedirect(reverse('index'))


def addauth(request):
    return render(request, 'addauth.html')

def addautorea(request):
    iz = request.POST["izena"]
    ab = request.POST["abizena"]
    jd = request.POST["jaiotze_data"]
    autoreberria = Liburuak(izena = iz, abizena=ab, jaiotze_data=jd)
    autoreberria.save()

    return HttpResponseRedirect(reverse('index'))
