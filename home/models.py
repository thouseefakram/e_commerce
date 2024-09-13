from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class data (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    date=models.DateField()
    
    def __str__(self):
        return(self.name)
     
class subdata(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    date=models.DateField()
    cat_id=models.ForeignKey(data, on_delete=models.CASCADE , related_name='subdata', db_column='cat_id')
  
         
    
    def __str__(self):
        return(self.name)


class Product(models.Model): 
    
    id=models.AutoField(primary_key=True)
    cat_id=models.ForeignKey(data, on_delete=models.CASCADE , related_name='product', db_column='cat_id')
    subcat_id=models.ForeignKey(subdata, on_delete=models.CASCADE, related_name='product', db_column='subcat_id')
    name=models.CharField(max_length=250)
    image= models.ImageField(upload_to="static")
    date=models.DateField(default=timezone.now)
    

    
    def __str__(self):
        return(self.name)

