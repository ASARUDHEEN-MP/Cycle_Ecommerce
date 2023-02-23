from django.urls import path
from . import views


urlpatterns = [
   path ('',views.index,name='index'),
   path ('login',views.login,name='login'),
   path ('signup',views.signup,name='signup'),
   path ('user_logout',views.user_logout,name='user_logout'),
   path('collections',views.collections,name='collections'),
   path('collections/<str:slug>',views.collection_view,name='collection_view'),
   path('collections/<str:cate_slug>/<str:prod_slug>',views.product_view,name='product_view'),
   #search
   path('product-list',views.productlistsajax),
   path('serachprdct',views.serach_prdct,name="serachprdct"),
   #cart
   path('add-to-cart',views.addtocart,name='addtocart'),
   path('cart',views.cart,name='cart'),
   path('delete_cart/<int:id>',views.delete_cart,name='delete'),
   path('updatecart',views.updatecart,name='updatecart'),
        

  #checkout
  path('checkout',views.checkout,name='checkout'),
 

 #userdetails
 path('userdetail',views.userdetail,name="userdetails"),
 path('addaddress',views.addaddress,name='addaddress'),
 path('deleteaddress/<int:pk>',views.delete_address,name='delete_address'),
 path('editaddress/<int:pk>',views.edit_address,name='edit_address'),
#  path('passwordreset',views.passwordreset,name="passwordreset"),



 #orders-------------

path('test',views.test,name="test"),
path('default/<int:id>',views.default,name="default"),
path('placeorder',views.placeorder,name="placeorder"),
path('orderview',views.orderview,name="orderview"),
path('view_order/<str:tr_id>',views.vieworder,name="vieworder"),
path('cancelorders/<int:pk>',views.cancelorders,name="cancelorders"),
path('orderdel',views.orderdel,name="orderdel"),

#onlinepay----------------
path('proceed-to-pay',views.razorpay),
path('pay',views.pay,name="pay"),

#test
path('my-response',views.my_orders,name="my_orders"),
path('applycoupon',views.applycoupon,name="applycoupon"),


path('change_password',views.change_password,name="change_password"),
path('about',views.about,name="about"),


   
   

]