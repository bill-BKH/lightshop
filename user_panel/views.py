from django.shortcuts import render, redirect , HttpResponse
from cart.models import Cart , CartDetail
from django.http import JsonResponse, HttpResponse
from .models import Address
from .forms import AdressesForm
from django.urls import reverse
import json
from account.models import User
from .forms import PersonalForm
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
  
def addresses(request):
    if request.method=='POST':
        form =AdressesForm(request.POST)
        if form.is_valid():
            receiver_name =form.cleaned_data['Receiver_full_name']
            receiver_num=form.cleaned_data['Receiver_number']
            receiver_state=form.cleaned_data['Receiver_state']
            receiver_city=form.cleaned_data['Receiver_city']
            receiver_Postal_address=form.cleaned_data['receiver_Postal_address']
            receiver_Postal_code=form.cleaned_data['receiver_Postal_code']
            address = Address.objects.create(user=request.user,receiver_name = receiver_name,receiver_num=receiver_num,receiver_state=receiver_state,
            receiver_city=receiver_city,receiver_Postal_address=receiver_Postal_address,receiver_Postal_code=receiver_Postal_code)
            address.save()
            return redirect(reverse('user_panel:address'))
    else:
        form = AdressesForm()
        user_address =Address.objects.filter(user=request.user)
        return render(request,'user_panel/profile-addresses.html',{'form': form , 'Address':user_address})

def delete_user_address(request):    
        data = json.loads(request.body.decode('utf-8'))
        address_id = data.get('addressid')
        user_address = Address.objects.filter(user=request.user,id=address_id).first()
        user_address.delete()
        return JsonResponse({'data':'success'})

def profile_info (request):
    info = User.objects.get(username = request.user)
    print(request.user)
    return render(request,'profile-personal-info.html',{info:'info'})
    

def profile_edit (request):
    form = PersonalForm()
    if request.method == 'POST':
        form = User.objects.get(username = request.user)
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            form = PersonalForm()
            context = {form:'form'}
            print(request.user)
            return render(request,'profile-additional-info.html',context)
    
    return render(request,'profile-additional-info.html',{form : 'form'})
