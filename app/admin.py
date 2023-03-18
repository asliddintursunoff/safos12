from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.admin import DateFieldListFilter


class MagazinAdmin(admin.ModelAdmin):
    
    list_per_page=10
    search_fields=['magazin']
admin.site.register(Magazinlar, MagazinAdmin)

class MahsulotAdmin(admin.ModelAdmin):
    list_display=["image","mahsulot_nomi","narx"]
    list_per_page=10
    
    
    search_fields=['mahsulot_nomi']

    def image(self,obj):
        return format_html('<img src="{0}" width="auto" height="150px">'.format(obj.rasm.url))
admin.site.register(Mahsulotlar, MahsulotAdmin)



class TotalAdmin(admin.ModelAdmin):
	
   change_list_template = "total.html"
   list_display=["dukon","mahsulot_nomi","mahsulot_soni","umumiy_narx","olingan_pul","qarz_olindi","qarzdorlik","sana"]
   list_per_page=10
    
   search_fields=('dukon__magazin',"mahsulot__mahsulot_nomi","mahsulot_soni","olingan_pul","sana")
   
admin.site.register(Savdo,TotalAdmin)  



class XarajatAdmin(admin.ModelAdmin):
	
   change_list_template = "xarajat.html"
   list_display=["kun","sabab","narx"]
   list_per_page=10
    
   search_fields=("kun","sabab","narx")
    
admin.site.register(Xarajat,XarajatAdmin)  


