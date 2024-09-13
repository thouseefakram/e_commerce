from django.contrib import admin
from home.models import data, subdata , Product

# Register your models here.
class product (admin.ModelAdmin):
    list_display=['id','name','date']
    
    
admin.site.register(data,product)


class products (admin.ModelAdmin):
    list_display=['id','name','cat_id','date']
    
    
admin.site.register(subdata,products)



class producting (admin.ModelAdmin):
    list_display=['id','cat_id','subcat_id','name','image','date']
    
    
admin.site.register(Product,producting)