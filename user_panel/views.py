from django.shortcuts import render
from cart.models import Cart , CartDetail

# Create your views here.
def user_profile(request):
    pass

def carts(request):
    user_carts = Cart.objects.filter(user=request.user)
    all = []
    for carts in user_carts:
             all.append(carts)

    return render(request , "user_panel/profile-orders.html" , {"datas" : all})

def detail(request , id):
    data = Cart.objects.get(id=id)
    return render(request , 'user_panel/cart_detail.html',{"user_cart_details" : data })
