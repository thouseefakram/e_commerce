from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect,JsonResponse
from home.models import data, subdata, Product
from datetime import datetime


# Create your views here.
def home (request):
    return render(request,'home.html')


def category(request):
    if request.method=="POST":
        
        name=request.POST.get('name')
        Data=data(name=name,date=datetime.today())
        Data.save()
    return render(request,'category.html') 

def show_cat(request):
    Data=data.objects.all()
    return render(request,'show_cat.html',{'Data':Data})

def del_cat(request):
    if 'id' in request.GET:
        id=request.GET.get('id')
        data.objects.filter(id=id).delete()
    return HttpResponseRedirect('/show_cat')

def edit_cat(request):
    if 'id' in request.GET:
        id=request.GET.get('id')
        for d in data.objects.filter(id=id):
            name=d.name
        return render(request,'edit_cat.html',{'name':name,'id':id,})
    
    
def record_edit(request):
    if 'id' in request.POST:
        id=request.POST.get('id')
        name=request.POST.get('name')
        date=datetime.today()
        data.objects.filter(id=id).update(name=name,date=date)
    return HttpResponseRedirect('/show_cat')





def subcategory(request):
    if request.method == "POST":    
        name = request.POST.get('name')
        cat_id = request.POST.get('cat_id')
        category=data.objects.get(id=cat_id)
        subcategory = subdata(name=name, cat_id=category,date=datetime.now())
        subcategory.save()
        return redirect('show_subcat')
    Data = data.objects.all()
    return render(request, 'subcategory.html', {'category': Data})

      
def show_subcat(request):

    sd=subdata.objects.all()
    return render(request,'show_subcat.html',{'sd':sd})


def del_subcat(request):
    if 'id' in request.GET:
        id=request.GET.get('id')
        subdata.objects.filter(id=id).delete()
    return HttpResponseRedirect('/show_subcat')

def edit_subcat(request):
    if 'id' in request.GET:
        id=request.GET.get('id')
        Data = data.objects.all()
        for d in subdata.objects.filter(id=id):
            name=d.name
        return render(request,'edit_subcat.html',{'name':name,'id':id,'category':Data})
    
   
    
    
def record_subedit(request):
    if 'id' in request.POST:
        id=request.POST.get('id')
        name=request.POST.get('name')
        cat_id=request.POST.get('cat_id')
        date=datetime.today()
        subdata.objects.filter(id=id).update(name=name,date=date,cat_id=cat_id)
    return HttpResponseRedirect('/show_subcat')






 
 
 


def product(request):
    if request.method=="POST":
        name=request.POST.get('name')
        cat_id=request.POST.get('cat_id')
        category=data.objects.get(id=cat_id)
        subcat_id=request.POST.get('subcat_id')
        subcategory=subdata.objects.get(id=subcat_id)
        image = request.FILES.get('image')
        pro=Product(name=name,image=image,cat_id=category,subcat_id=subcategory)
        pro.save()
        return redirect('show_product')
    Data = data.objects.all()
    Subdata=subdata.objects.all()
    return render(request, 'product.html', {'category': Data,'subcategory':Subdata}) 

def show_product(request):
    
    pro=Product.objects.all()
    return render(request,'show_product.html',{'pro':pro})


def del_product(request):
    if 'id' in request.GET:
        id=request.GET.get('id')
        Product.objects.filter(id=id).delete()
    return HttpResponseRedirect('/show_product')

def edit_product(request):
    if 'id' in request.GET:
        id=request.GET.get('id')
        image = request.FILES.get('image')
        Data=data.objects.all()   
        Subdata=subdata.objects.all()
        for p in Product.objects.filter(id=id):
            name=p.name
        return render(request,'edit_product.html',{'name':name,'id':id,'category':Data,'subcategory':Subdata,})
                                         

def record_product(request):
    if 'id' in request.POST:
        id = request.POST.get('id')
        name = request.POST.get('name')
        image = request.FILES.get('image')   
        cat_id = request.POST.get('cat_id')
        subcat_id = request.POST.get('subcat_id')
        date = datetime.today()
        product = Product.objects.get(id=id)
        product.name = name
        product.cat_id = cat_id
        product.subcat_id = subcat_id
        product.date = date
        if image:  # Check if a new image was uploaded
            product.image = image
        product.save()
        return HttpResponseRedirect('/show_product')




def ajax_handler(request,id):
    sub_data = subdata.objects.filter(cat_id=id).values_list('id','name')
    print(sub_data)
    sub_data = dict(sub_data)
    return JsonResponse({
        'subdata' : sub_data,
    })