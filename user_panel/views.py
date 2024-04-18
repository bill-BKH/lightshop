from django.shortcuts import render, redirect , HttpResponse
from .models import AddAddress
from .forms import AdressesForm
from django.urls import reverse
# Create your views here.
def user_profile(request):
    pass

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


