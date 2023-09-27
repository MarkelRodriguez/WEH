from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('addlib/', views.addlib, name='addlib'),
    path ('addlib/addliburua/', views.addliburua, name='addliburua'),
    path ('addauth/', views.addauth, name='addauth'),
    path ('addauth/addautorea/', views.addautorea, name='addautorea')
    #path('ezabatu/<int:id>', views.deletepost,name='deletepost'),
    #path('update/<int:id>/',views.update ,name='update'),
    #path('updatepost/<int:id>',views.updatepost ,name='updatepost'),

    
]