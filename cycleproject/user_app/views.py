# Create your views here.
from django.shortcuts import render,redirect
from . models import *
from hashlib import sha256
from django.contrib.auth import authenticate
from django.contrib import messages,auth 
from django.views.decorators.cache import cache_control
from category.models import Categorys,products,product_list
from admin_app.models import carosuel
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from django.core.validators import EmailValidator

from.form import send_forget_password_mail
# Create your views here.
@cache_control(no_cache = True,must_revalidate = False,no_store = True)
def index(request):
    categorys = Categorys.objects.filter(status=0)
    
    context={'categorys':categorys}
    return render(request,'user/index1.html',context)

@cache_control(no_cache =True, must_revalidate =False, no_store =True)
def login(request):
    if 'username' in request.session:
        return redirect('user:home')
   
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = authenticate(username = username,password = password)

        except:
            user = None
            pass
        if user is not None :
            auth.login(request,user)
            request.session['username']= username
            messages.info(request,'logged in successfully')
            return redirect(index)
        else:
            messages.success(request,'invalid loginrequest')
            return redirect('login')

    return render(request,'login.html')
    


#signup
def signup(request):
    if 'username' in request.session:
        return redirect(index)
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if username == '':
                 messages.info(request,'username is empty')
                 return redirect(signup)
        elif email == '':
                messages.info(request,'Email is empty')
                return redirect(signup)
        elif password == '':
                messages.info(request,'password is empty')
                return redirect(signup)
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('index')

    return render(request,'signup.html')
    

# @cache_control(no_cache = True,must_revalidate = False,no_store = True)
# def signup(request):
#     global x
#     if 'username' in request.session:
#         return redirect(index)
#     if request.method =='POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         mobile=request.POST.get('phonenumber')
#         password=request.POST.get('password')
#         if username == '':
#                 messages.info(request,'username is empty')
#                 return redirect(signup)
#         elif email == '':
#                 messages.info(request,'Email is empty')
#                 return redirect(signup)
#         elif password == '':
#                 messages.info(request,'password is empty')
#                 return redirect(signup)
        
#         if myuser.objects.filter(email=email):
#                 messages.info(request,'Email is already taken')
#         myuser(username=username,email=email,mobile=mobile,password=password).save()
#         return redirect(login)
        
#     return render(request,'signup.html')
#def verify_otp(request):
    #if 'username' in request.session:
        #return redirect('user:home')

    #if request.method =='POST':
       # get_otp = request.POST.get('otp')
       # phone_number =  request.session['mobile'] 
        
        #if check_otp(phone_number,get_otp):

            #first_name =   request.session['username'] 
             #email =    request.session['email'] 
            #mobile =    request.session['mobile'] 
            #password =    request.session['password'] 

            #del request.session['email']
            #del request.session['username']
           #del request.session['mobile'] 
           # del request.session['password']

            #user = myuser.objects.create_user(username=username,mobile=mobile,email=email,password=password)
            #user.save()
            #return redirect()
        #else:
           # messages.info(request,'invalid otp number')
    #return render(request,'register_otp.html')




@cache_control(no_cache = True,must_revalidate = False,no_store = True)
def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
        messages.info(request,'logout successfully')
        return redirect(index)
        

#categry
def collections(request):
    categorys = Categorys.objects.filter(status=0)
    context={'categorys':categorys}
    return render(request,'categories.html',context)


#collections

   
def collection_view(request,slug):
   if(Categorys.objects.filter(slug=slug,status=0)):
      productt=product_list.objects.filter(category__slug=slug)
      cat_name=Categorys.objects.filter(slug=slug).first()
      contexts = {'productt':productt,'cat_name':cat_name}
      return render(request,'user/collections_view.html',contexts)
   else:
    messages.warning(request,"no such file")
    return redirect('collections')
#single productdetails

def product_view(request,cate_slug,prod_slug):
    if(Categorys.objects.filter(slug=cate_slug,status=0)):
         if(product_list.objects.filter(slug=prod_slug,status=0)):
            product=product_list.objects.filter(slug=prod_slug,status=0).first
            context={'product':product}
            
    


         else:
           
            return redirect('collections')


    else:
        
        return redirect('collections')
   
    return render(request,'user/single_product.html',context)



#cart managment ---------------------------------------------------------------------
def addtocart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check= product_list.objects.get(id=prod_id)
            print("hello")

            if(product_check):
                    if(carts.objects.filter(user=request.user.id,product_id=prod_id)):
                        return JsonResponse({'status':"product already in cart"})

                
                
                 
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        dd = request.user
                        
                        carts.objects.create(user=dd,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"product added successfully"})
                    else:
                        return JsonResponse({'status':"only "+str(product_check.quantity)+"quantity available"})


            else:
                return JsonResponse({'status':"no such product found"})

             

        else:
            return JsonResponse({'status':"login to continue"})
    return redirect('index')

def cart(request):
    dd = request.user
    cart_items = carts.objects.filter(user = dd)
    context={'cart_items':cart_items}
    
    return render(request,'user/cartview.html',context)



def delete_cart(request,id):
    my=carts.objects.get(id=id)
    my.delete()
    return redirect('cart')

def updatecart(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        userss=request.user
        users_id=request.user.id
        if(carts.objects.filter(user_id=userss,product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart=carts.objects.get(user_id=users_id,product_id=prod_id)
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({'status':"update to continue"})
        
        return redirect('index')

#checkout----------------------------------
def checkout(request):
    user = request.user
    total=0
    grand_total = 0
    dd=request.user
    discount = 0
    addrssz=userdetails.objects.filter(is_default=True,user=request.user)
    cartitems=carts.objects.filter(user=dd)
    address=userdetails.objects.filter(user=dd)

    for item in cartitems:
        total +=item.product.price * item.product_qty
    print(total)
    if 'coupons' in request.session:
        print('coupon')
        coupons=request.session['coupons']
        print(coupons)
        coup = coupon.objects.get(coupon_code=coupons)
       
        discount = coup.discount
        print(discount)
        messages.info(request,'')
        
        Used_Coupon.objects.create(user = user,coupon = coup )
    
    

   
        
        
       

    m=total
    grand_total = total-discount
    print(grand_total)
    context={'cartitems':cartitems,'grand_total':grand_total,'address':address,'addrssz':addrssz,'discount':discount,'m':m}
    return render(request,'user/usercheckout.html',context)







#userdetails----------------
def userdetail(request):
    d=request.user
    idss=request.user.id
    users = User.objects.get(username=d)
    address=userdetails.objects.filter(user=idss)
    context={'users':users,'address':address}
    return render(request,'user/userdetails.html',context)


def addaddress(request):
    d=request.user
    users = User.objects.get(username=d)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        state = request.POST['state']
        country = request.POST['country']
        city = request.POST['city']
        pincode = request.POST['pincode']
        user = users
        hh=len(phone)
        if hh!=10:
            messages.info(request,"enter 10 digit number for phonenumber ")
            return redirect('addaddress')
    
        else:
            newaddress=userdetails.objects.create( fname = fname,
                                               lname=lname,
                                               email = email,
                                               phone=phone,
                                               address=address,
                                               state = state,
                                               city =city,
                                               pincode=pincode,
                                               country=country,
                                               user=user)
            newaddress.save()
       
        return redirect(userdetail)
           

        
        
        
    

    return render(request,'user/addaddress.html')

def delete_address(request,pk):
    address=userdetails.objects.get(id=pk)
    address.delete()
    return redirect(userdetail)

def edit_address(request,pk):
    address=userdetails.objects.get(id=pk)
    dd=request.user
    userz=User.objects.get(username=dd)
    context={'userz':userz,
       'address':address
    }
    if request.method == 'POST':
       address.fname = request.POST['fname']
       address. lname = request.POST['lname']
       address.email = request.POST['email']
       address.phone = request.POST['phone']
       address.state = request.POST['state']
       address.country = request.POST['country']
       address.city = request.POST['city']
       address.pincode = request.POST['pincode']
       address.address = request.POST['address']

       address.save()
       return redirect(userdetail)
    return render(request,'user/editaddress.html',context)    



# def passwordreset(request):
#     if request.method == 'POST':
#         Current = request.POST['Current Password']
#         New = request.POST['New Password']
#         confirm=request.POST['conf Password']
#         return redirect('index')
#     return render(request,'user/resetpassword.html')





    


 #orders---------------------------------
# @login_required(login_url='login')
# def order(request):



def test(request):
    dd=request.user
    address=userdetails.objects.filter(user=dd)
    context={
        'address':address

    }
    return render(request,'test.html',context)


#addess set up for order----
def default(request,id):
    dd=request.user
    address=userdetails.objects.filter(user=dd)
    defaultaddress=userdetails.objects.get(id=id)
    defaultaddress.is_default=True
    defaultaddress.save()
    
    for i in address:
        if i != defaultaddress:
            i.is_default=False
            i.save()
            

    return redirect('checkout')


#placeorder------

@csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
def placeorder(request):
    print('first')
    print('payment_mod')
    total=0
    discount=0
    
    cart_total_price = 0
    dd=request.user
    payment_mod='NOT'
    payment_id='none'
    dd_id=request.user.id
    user_ids=User.objects.get(username=dd)
    addrssz=userdetails.objects.filter(is_default=True,user=request.user)
    cart_ids=carts.objects.filter(user=dd_id)
    tracking_no =( random.randint(100000,999999))
    if request.method == 'POST':
      
        payment_mod= request.POST.get('payment_mode')
        payment_id= request.POST.get('payment_id')
        print('second')
        print(payment_mod)
    if 'coupons' in request.session:
        print('coupon')
        coupons=request.session['coupons']
        coup = coupon.objects.get(coupon_code=coupons)
        discount = coup.discount
        del request.session['coupons']
        print(coup.discount)
       
    
    print('hello')
    
    for item in cart_ids:
        cart_total_price=total+item.product.price*item.product_qty
    

    cart_total_price -=discount
    print(cart_total_price)
    orders = order.objects.create(
       user=request.user,
       total_price=cart_total_price,
       address=userdetails.objects.get(is_default=True,user=request.user),
       tracking_no=tracking_no,
       payment_mode=payment_mod,
       payment_id=payment_id,
       status='Confirmed',
    )
    orders.save()
    ordersitem = orderitem.objects.create(
        user=request.user,
        orderit=orders,
        product=item.product,
        price=item.product.price,
        quantity=item.product_qty,
        
    )
    ordersitem.save()
    #dcsrc quantiy from admin stock
    productz=product_list.objects.filter(id=item.product_id).first()
    productz.quantity=productz.quantity-item.product_qty
    productz.save()
    cart_ids.delete()
    messages.info(request,'your oder is successfull')
    
    ff={
          'user_ids':user_ids,
          'addrssz':addrssz,
          'cart_ids':cart_ids,
    }
    paymode=request.POST.get('payment_mode')
    if (paymode=='COD'):
        return redirect("/")
    if(paymode=="paid by razorpay"):
         return JsonResponse({'status':"your oder is successfull"})
        
    return render(request,'orders/orderview.html',ff)

#show myorder

def orderview(request):
    u=request.user
    oderz=order.objects.filter(user=u)
    ff={
        'oderz':oderz
    }
    return render(request,'orders/orderview.html',ff)


def vieworder(request,tr_id):
    
    ord=order.objects.filter(tracking_no=tr_id).filter(user=request.user).first()
    ord_itm=orderitem.objects.filter(orderit=ord)
    for item in ord_itm:
        pr=item.price
    
    discount=ord.total_price - pr
 
    context={'ord':ord,'ord_itm':ord_itm,'discount':discount}
    
    return render(request,'orders/userorderview.html',context)


def cancelorders(request,pk):
    if request.user.is_authenticated:
        orders=order.objects.get(id=pk)
        orders.status = 'Cancelled'
        orders.save()
        ord_itm=orderitem.objects.filter(orderit=orders.id)
        for i in ord_itm:
             i.status = 'Cancelled'
             i.save()

        return redirect('orderview')
    

def orderdel(request):
    ords=order.objects.filter(user=request.user).first()
    if ords.status == 'Cancelled':
        ords.delete()
    return redirect('orderview')


@csrf_exempt
def razorpay(request):
    dd=request.user
    cart=carts.objects.filter(user=dd)
    
    total_price=0
    for item in cart:
        total_price=total_price+item.product.price*item.product_qty


    return JsonResponse({
        'total_price':total_price
    })
    
@csrf_exempt
def pay(request):
    return redirect('placeorder')

#test
@csrf_exempt
def my_orders(request):
    return HttpResponse("my order page")



#coupon
def applycoupon(request):
    print('hello')
    # if coupon in request.session:
    #     messages.info(request,'only one coupon is allowed')
    #     return redirect("checkout")

    if request.method == 'POST':
       
        coupons=request.POST.get("coupon")
        coup=coupon.objects.filter(coupon_code=coupons)
        print(coupons)
     
        print('visted 123opooppo')
        # try:
        #     used_coupon = Used_Coupon.objects.get(user=request.user,coupon = coup)
        #     if used_coupon:
        #          print('visted 123')
        #          messages.info(request,'Coupon already used')
        #          return redirect("checkout")
        # except:
        #     print('jhgjhgjhgjh')

        if coup:
            print('visted')
            request.session['coupons'] = coupons
            return redirect("checkout")
        else:
            messages.info(request,'invalid coupon')
            print('invalid')
            return redirect("checkout")
                 

def change_password(request,token):
   
    try:
        profile_obj = User.objects.filter(forgot_password_token=token).first()
        print(profile_obj)
        context = {'user_id': profile_obj.id}

        if request.method == "POST":
            new_password = request.POST['password1']
            confirm_password = request.POST['password2']
            user_id = request.POST['user_id']


            if user_id is None:
                messages.info(request,'no user found')
                return redirect(f'/change_password/{token}/')
            if  new_password !=  confirm_password:
                messages.info(request,'password dosent match')
                return redirect(f'/change_password/{token}/')
            

            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            del request.session['username']
            return redirect('/')

        
    except Exception as e:
        print(e)

    return render(request,'user/resetpassword.html',context)




#--------------------------search---------------------------------------------#
def productlistsajax(request):
    serch=product_list.objects.filter(status=0).values_list('name',flat=True)
    prdctlist=list(serch)
    return JsonResponse(prdctlist,safe=False)

def serach_prdct(request):
    if request.method == 'POST':
        searchtest=request.POST['srchbarprdt']
        if searchtest=="":
           return redirect(request.META.get('HTTP_REFERER'))
        else:
            product=product_list.objects.filter(name__contains=searchtest).first()
            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request,'Product NOT FOUND')
                return redirect(request.META.get('HTTP_REFERER'))
 
    return redirect(request.META.get('HTTP_REFERER'))



#--------------------------about-------------------------------
def about(request):
    return render(request,'user/About.us.html')

