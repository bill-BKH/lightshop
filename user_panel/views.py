from django.shortcuts import render
from cart.models import Cart , CartDetail

# Create your views here.
def user_profile(request):
    pass

def carts(request):
    user_carts = Cart.objects.filter(user=request.user.id)
    return render(request , "user_panel/profile-orders.html" , {"datas" : user_carts})
def detail(request , id):
    cart = Cart.objects.filter(id=id).first()
    cart_details =cart.cartdetail_set.all()
    return render(request , 'user_panel/cart_detail.html',{"user_cart_details" : cart_details })
