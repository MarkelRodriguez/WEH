from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('addlib/', views.addlib, name='addlib'),
    path ('addlib/addliburua/', views.addliburua, name='addliburua'),
    path ('addauth/', views.addauth, name='addauth'),
    path ('addauth/addautorea/', views.addautorea, name='addautorea'),
    path('deleteliburua/<int:id>/', views.deleteliburua,name='deleteliburua'),
    path('deleteautorea/<int:id>/', views.deleteautorea,name='deleteautorea'),
    path('updatelib/<int:id>/',views.updatelib ,name='updatelib'),
    path('updateliburua/<int:id>',views.updateliburua ,name='updateliburua'),
    path('updateauth/<int:id>/',views.updateauth ,name='updateauth'),
    path('updateautorea/<int:id>',views.updateautorea ,name='updateautorea'),

    
]