from django.shortcuts import render
from product.models import Product
import json
from django.http import JsonResponse,HttpResponse

# Create your views here.
def search(request):
    print('ok i have a reques')
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        product_title = data.get('product_title')
        # print(product_title)
        searched_product = Product.objects.filter(title__icontains=product_title).values_list('title','slug','main_picture')
        print(searched_product)
        return JsonResponse({'data':list(searched_product)})
        print(request.POST)
    else:
        return render(request,'search/index.html')

    
    # data = json.loads(request.body.decode('utf-8'))
    # product_id = data.get("product_id")


def price_filter(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        price_range = data.get('price_range').replace(',','').split(' - ')
        print(data)
        print('-'*90)
        filterd_product = Product.objects.filter(price__range=(int(price_range[0]),int(price_range[1])))
        print(filterd_product.values())
    print(request.GET)
    return render(request, 'search.html')
