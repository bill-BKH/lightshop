from django.shortcuts import render
from django.http import HttpResponse
from product.models import ProductCategory

# Create your views here.
def index(request):
    return render(request, 'shop/index.html') 


def catogory_shard(request):
    context = {'category_list':ProductCategory.objects.all()}
    return context