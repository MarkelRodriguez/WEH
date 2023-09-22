from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Post

# Create your views here.
def index(request):

    postak = Post.objects.all
    return render(request, 'index.html', {'posta':postak})

def add(request):
    return render(request, 'add.html')

def addpost(request):
    iz = request.POST["izenburua"]
    ed = request.POST["edukia"]
    postberria = Post(izenburua = iz, edukia=ed, noizsortua="")
    postberria.save()

    return HttpResponseRedirect(reverse('index'))

def deletepost(request, id):
    deleteid = Post.objects.get(id = id)
    Post.delete(deleteid)
    
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    
    #updateid = Post.objects.get(id = id)
    return render(request, 'update.html', {'id':id})

def updatepost(request,id):
    updateid = Post.objects.get(id = id)
    iz =  request.POST["izenburua"]
    ed = request.POST["edukia"]

    updateid.izenburua = iz
    updateid.edukia = ed
    updateid.save()
    return HttpResponseRedirect(reverse('index'))