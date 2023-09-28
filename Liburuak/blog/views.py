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

def addliburua(request):
    autoreaid = request.POST["autorea"]
    iz = request.POST["izenburua"]
    ed = request.POST["edukia"]
    au = Autoreak.objects.get(id = autoreaid)
    liburuberria = Liburuak(izenburua = iz, edukia=ed, noizsortua="",autorea=au)
    liburuberria.save()
    
    return HttpResponseRedirect(reverse('index'))


def addauth(request):
    return render(request, 'addauth.html')

def addautorea(request):
    iz = request.POST["izena"]
    ab = request.POST["abizena"]
    jd = request.POST["jaiotze_data"]
    autoreberria = Autoreak(izena = iz, abizena=ab, jaiotze_data=jd)
    autoreberria.save()

    return HttpResponseRedirect(reverse('index'))

def updatelib(request,id):
    liburua = Liburuak.objects.get(id = id)
    autoreak = Autoreak.objects.all
    return render(request, 'updatelib.html', {'id':id,'autoreak':autoreak, 'liburua':liburua})

def updateliburua(request,id):
    updateid = Liburuak.objects.get(id = id)
    
    iz =  request.POST["izenburua"]
    ed = request.POST["edukia"]
    autoreaid = request.POST["autorea"]
    autorea = Autoreak.objects.get(id = autoreaid)
    updateid.izenburua = iz
    updateid.edukia = ed
    updateid.autorea = autorea

    updateid.save()
    return HttpResponseRedirect(reverse('index'))

def updateauth(request,id):
    autorea = Autoreak.objects.get(id = id)
    return render(request, 'updateauth.html', {'id':id, 'autorea':autorea})

def updateautorea(request,id):
    updateid = Autoreak.objects.get(id = id)
    iz =  request.POST["izena"]
    ab = request.POST["abizena"]
    jd = request.POST["jaiotze_data"]
    updateid.izena= iz
    updateid.abizena = ab
    updateid.jaiotze_data = jd
    updateid.save()
    return HttpResponseRedirect(reverse('index'))

def deleteliburua(request,id):
    deleteid = Liburuak.objects.get(id = id)
    Liburuak.delete(deleteid)
    
    return HttpResponseRedirect(reverse('index'))


def deleteautorea(request,id):
    deleteid = Autoreak.objects.get(id = id)
    Autoreak.delete(deleteid)
    
    return HttpResponseRedirect(reverse('index'))

