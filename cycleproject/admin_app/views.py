from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from user_app.models import myuser
from category.models import Categorys,products,product_list
from . models import carosuel
from django.contrib import messages 
from django.contrib.auth.models import User
from user_app.models import *
from . forms import ProductForm,categoryForm,orderForm



# Create your views here.
def admindashboard(request):
    return render(request,'admindashboard.html')


@cache_control(no_cache = True,must_revalidate = False,no_store = True)
def adminlogin(request):
    if 'user' in request.session:
        return redirect(adminpanel)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user is not None:
           if  user.is_superuser:
                request.session['user'] = username
                return redirect(adminpanel)
        else:
            messages.info(request,'you are not an admin')
            return redirect(adminlogin)
    
            
        
    return render(request,'adminlogin.html') 

@cache_control(no_cache = True,must_revalidate = False,no_store = True)
def adminpanel(request):
    
    return render(request,'admin_templates/admin_dashboard.html')

@cache_control(no_cache = True,must_revalidate = False,no_store = True)
def logout(request):
    if 'user' in request.session:
        request.session.flush()
    return redirect(adminlogin)


#usermanagment------
def user_mgmt(request):
    users = User.objects.filter(is_superuser=False)
    return render(request,'admin_templates/usermanagment.html',{'users':users})

def block_user(request,pk):
    user = User.objects.get(id =pk)
    user.is_active = False
    user.save()
    print('user blocked')
    return redirect('user_mgmt')

def unblock_user(request,id):
    user = User.objects.get(id= id)
    user.is_active  = True
    user.save()
    print('user is active')
    return redirect('user_mgmt')
 
def delete(request,id):
    my=User.objects.get(id=id)
    my.delete()
    return redirect('user_mgmt')





#categories
def view_category(request):
    category = Categorys.objects.all()
    return render(request,'admin_templates/category.html',{'category':category})

def deletes(request,id):
    pop=Categorys.objects.get(id=id)
    pop.delete()
    return redirect('view_category')


def addcategory(request):
    form = categoryForm()

    if request.method == 'POST':
        form = categoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_category')
    else:
        form = categoryForm()

    context = {
        "form":form
    }

    return render(request, 'admin_templates/add_category.html', context)



def updatecatgory(request,pk):
    Category = Categorys.objects.get(id=pk)
    
    form = categoryForm(instance=Category)

    if request.method == 'POST':
        form = categoryForm(request.POST, request.FILES, instance=Category)
        if form.is_valid():
            form.save()
            return redirect('collection_list')

    context = {
        "form":form
    }

    return render(request, 'admin_templates/update_Product.html', context)


#PRODUCT collection

def collection_list(request):
    product = product_list.objects.all()
    return render(request,'admin_templates/collection_list.html',{'product':product})

def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collection_list')
    else:
        form = ProductForm()

    context = {
        "form":form
    }

    return render(request, 'admin_templates/add_collection.html', context)
    

def updateProduct(request,pk):
    product = product_list.objects.get(id=pk)
    
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_category')

    context = {
        "form":form
    }

    return render(request, 'admin_templates/update_category.html', context)


 
def deletesss(request,id):
    my=product_list.objects.get(id=id)
    my.delete()
    return redirect('collection_list')



#carousel
def view_carousel(request):
    product = carosuel.objects.all()
    return render(request,'admin_templates/carouel_list.html',{'product':product}
    )


#------------------------------------order-------------------------------------------------------------------------------------------
def orders(request):
    ord=order.objects.all()
    return render(request,'admin_templates/orderllist.html',{"ord":ord})

def ordstatus(request,id):
    ord=order.objects.get(id=id)
    if  ord.status =='Confirmed':
        ord.status='Shipped'
    elif ord.status =='Shipped':
         ord.status='Out_for_delivery'
    elif ord.status =='Out_for_delivery':
         ord.status='Delivered'
    elif ord.status =='Delivered':
         ord.status='Returned'
    ord.save()
    print(ord)
    return redirect('orders')

def canclorder(request,id):
    ord=order.objects.get(id=id)
    ord.status='Cancelled'
    ord.save()
    return redirect('orders')

def deleteord(request,id):
    ord=order.objects.get(id=id)
    ord.delete()
    return redirect('orders')


def vieworders(request,tr_id):
    ord=order.objects.filter(tracking_no=tr_id).filter(user=request.user).first()
    ord_itm=orderitem.objects.filter(orderit=ord)
    for item in ord_itm:
        pr=item.price
   
    
    discount=ord.total_price - pr
 
    context={'ord':ord,'ord_itm':ord_itm,'discount':discount}
    
    return render(request,'admin_templates/orderview.html',context)
    
 
def canceledorders(request):
    ord=order.objects.filter(status='Cancelled')
    context={'ord':ord}
    
    return render(request,'orders/cancelorder.html',context)
    

#---------------------------------------------coupon--------------------------------------------------------------

def couponlist(request):
    coup=coupon.objects.all()
    return render(request,'admin_templates/couponview.html',{'coup':coup})

def addcoupon(request):
    form = orderForm()

    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('couponlist')
    else:
        form = orderForm()

    context = {
        "form":form
    }

    return render(request, 'admin_templates/add_coupon.html', context)
    
    
def activecp(request,pk):
    coup=coupon.objects.get(id=pk)
    print(coup)
    coup.is_active =True
    coup.save()
    return redirect('couponlist')

def deactivecp(request,id):
    coup=coupon.objects.get(id=id)
    coup.is_active =False
    coup.save()
    return redirect('couponlist')

def deletecp(request,id):
    coup=coupon.objects.get(id=id)
    coup.delete()
    return redirect('couponlist')



#-------------------------------------------------------



