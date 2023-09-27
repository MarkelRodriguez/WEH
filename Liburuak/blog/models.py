from django.db import models
# Create your models here.

class Autoreak(models.Model):
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    jaiotze_data = models.DateField()

    def __unicode__(self):
        return self.izena


class Liburuak(models.Model):
    izenburua = models.CharField(max_length = 100)
    edukia = models.CharField(max_length = 300)
    noizsortua = models.DateTimeField(auto_now_add = True)
    autorea =  models.ForeignKey(Autoreak, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.izenburua
    
