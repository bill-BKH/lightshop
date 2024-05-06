from django.shortcuts import render
from django.http import HttpResponse
from product.models import ProductCategory, Product
from product.models import ProductVisit
from utils.http_service import get_client_ip
# Create your views here.
def index(request):
    user_ip = get_client_ip(request)
    visited_product2 = ProductVisit.objects.filter(ip__iexact=user_ip)
    visited_product = [] 
    for visit in visited_product2:
        visited_product.append(Product.objects.get(id =visit.product.id))


    return render(request, 'shop/index.html',{'visited_product':visited_product})


def catogory_shard(request):
    context = {'category_list':ProductCategory.objects.all()}
    return context