from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addpost/', views.addpost, name='addpost'),
    path('ezabatu/<int:id>', views.deletepost,name='deletepost'),
    path('update/<int:id>/',views.update ,name='update'),
    path('updatepost/<int:id>',views.updatepost ,name='updatepost'),

    
]