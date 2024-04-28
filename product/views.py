from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,ProductCategory,ProductComment
from django.core.paginator import Paginator
from account.models import User

# Create your views here.

def product_detail(request, slug):
    data = Product.objects.get(slug=slug)
    comments = ProductComment.objects.filter(confirmed_by_admin=True)
    return render(request, 'product/single-product.html',{'product':data, 'comments': comments})

def home(request):
    products = Product.objects.all().order_by()
    paginator = Paginator(products, 4)
    page_obj = paginator.get_page(request.GET.get('page', 1))

    return render(request,'product/home.html',{'page_obj':page_obj, 'paginator':paginator})


def product_by_cat(request,category):
    category_obj = ProductCategory.objects.filter(url_title=category).first()
    products = Product.objects.filter(category=category_obj)
    paginator = Paginator(products, 4)
    page_obj = paginator.get_page(request.GET.get('page', 1))

    return render(request,'product/home.html',{'page_obj':page_obj, 'paginator':paginator})
    