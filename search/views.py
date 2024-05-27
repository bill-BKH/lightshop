from django.shortcuts import render
from product.models import Product
import json
from django.http import JsonResponse

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

