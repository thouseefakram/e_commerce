from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home),
    path('category',views.category,name="category"),
    path('show_cat',views.show_cat,name="show_cat"),
    path('del_cat',views.del_cat,name="del_cat"),
    path('edit_cat',views.edit_cat,name="edit_cat"),
    path('record_edit',views.record_edit,name="record_edit"),
    
    
    
    path('subcategory',views.subcategory,name="subcategory"),
    path('show_subcat',views.show_subcat,name='show_subcat'),
    path('del_subcat',views.del_subcat,name="del_subcat"),
    path('edit_subcat',views.edit_subcat,name="edit_subcat"),
    path('record_subedit',views.record_subedit,name="record_subedit"),
    
    
    path('product',views.product,name="product"),
    path('show_product',views.show_product,name="show_product"),
    path('del_product',views.del_product,name="del_product"),
    path('edit_product',views.edit_product,name="edit_product"),
    path('record_product',views.record_product,name="record_product"),
    path('ajax_handler/<int:id>/', views.ajax_handler, name="ajax_handler")
   

]
