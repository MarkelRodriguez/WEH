from django.contrib import admin
from .models import Autoreak,Liburuak

# Register your models here.


class AutoreakAdmin(admin.ModelAdmin):
    list_display = ['izena','abizena','jaiotze_data']


admin.site.register(Autoreak,AutoreakAdmin)

class LiburuakAdmin(admin.ModelAdmin):
    list_display = ['izenburua','edukia','noizsortua','autorea']


admin.site.register(Liburuak,LiburuakAdmin)