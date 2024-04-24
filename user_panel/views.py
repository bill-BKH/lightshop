<<<<<<< HEAD
from django.shortcuts import render, redirect , HttpResponse
from cart.models import Cart , CartDetail
from .models import AddAddress
from .forms import AdressesForm
from django.urls import reverse

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
            Address = AddAddress.objects.create(user=request.user,receiver_name = receiver_name,receiver_num=receiver_num,receiver_state=receiver_state,
            receiver_city=receiver_city,receiver_Postal_address=receiver_Postal_address,receiver_Postal_code=receiver_Postal_code)
            Address.save()
            return redirect(reverse('user_panel:address'))
    else:
        form = AdressesForm()
    user_address =AddAddress.objects.filter(user=request.user).first()

    return render(request,'user_panel/profile-addresses.html',{'form': form , 'UrAddress':user_address})
=======
from django.shortcuts import render,redirect
from account.models import User
from .forms import PersonalForm
# Create your views here.
def profile_info (request):
       info = User.objects.filter(email__iexact = 'sami000@gmail.com')
       return render(request,'profile-personal-info.html',{'info':info})
       
def profile_edit (request):
       form = PersonalForm()
       if request.method == 'POST':
              form = PersonalForm(request.POST)
              if form.is_valid:
                     form.save
                     form = PersonalForm()
                     return render(request,'profile-additional-info.html',{form : 'form'})
       else:
              return render(request,'profile-additional-info.html',{form : 'form'})

       
>>>>>>> a6c731b (commit message)
