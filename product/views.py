from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Product,ProductCategory,ProductComment
from django.core.paginator import Paginator
from account.models import User
import json

# Create your views here.

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    comments = ProductComment.objects.filter(confirmed_by_admin=True)
    product_related_category = ProductCategory.objects.get(id=product.category.all()[0].id)
    related_products = Product.objects.filter(category=product_related_category).order_by('-id')[:10]
    # print(product_related_category.id)
    # print(related_product)
    return render(request, 'product/single-product.html',{'product':product, 'comments': comments,'related_products':related_products})

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


def like(request):
    data = json.loads(request.body.decode('utf-8'))
    comment_id = data.get("comment_id")
    comment = ProductComment.objects.filter(id=comment_id).first()
    if comment.has_user_disliked(request.user):
        return JsonResponse({"data" : '0' })
    if comment.has_user_liked(request.user):
        like = comment.like
        new_like = like - 1
        ProductComment.objects.filter(id=comment_id).update(like=new_like)
        comment.user_liked.remove(request.user)
        return JsonResponse({"data" : '2' })
    else :
        like = comment.like
        new_like = like + 1
        ProductComment.objects.filter(id=comment_id).update(like=new_like)
        comment.user_liked.add(request.user)
        return JsonResponse({"data" : '1' })

       
    

def dislike(request):
    data = json.loads(request.body.decode('utf-8'))
    comment_id = data.get("comment_id")
    comment = ProductComment.objects.filter(id=comment_id).first()
    if comment.has_user_liked(request.user):
        return JsonResponse({"data" : '0' })
       
    if comment.has_user_disliked(request.user):
        like = comment.dislike
        new_like = like - 1
        ProductComment.objects.filter(id=int(comment_id)).update(dislike=new_like)
        comment.user_dislike.remove(request.user)
        return JsonResponse({"data" : '2' })
    else :
        like = comment.dislike
        new_dislike = like + 1
        ProductComment.objects.filter(id=int(comment_id)).update(dislike=new_dislike)
        comment.user_dislike.add(request.user)
        return JsonResponse({"data" : '1' })