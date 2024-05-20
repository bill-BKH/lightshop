from django.shortcuts import render
from django.http import HttpResponse
from product.models import ProductCategory, Product
from product.models import ProductVisit
from utils.http_service import get_client_ip
from .models import MainSlider
from django.db.models import Sum
from cart.models import Cart,CartDetail
# Create your views here.


def index(request):
    most_sold_products = Product.objects.filter(cartdetail__cart__is_paid=True).annotate(cart_count=Sum('cartdetail__count')).order_by('-cart_count')[:10]
    user_ip = get_client_ip(request)
    visited_product2 = ProductVisit.objects.filter(ip__iexact=user_ip)
    visited_product = [] 
    for visit in visited_product2:
        visited_product.append(Product.objects.get(id =visit.product.id))
    mainslider=MainSlider.objects.all()


    return render(request, 'shop/index.html',{'visited_product':visited_product, "most_solds":most_sold_products,'mainslider':mainslider})


def catogory_shard(request):
    context = {'category_list':ProductCategory.objects.all()}
    return context