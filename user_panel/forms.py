from django import forms
from .models import AddAddress

class AdressesForm(forms.Form):
    Receiver_full_name = forms.CharField(
        label='نام و نام خانوادگی ',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی گیرنده را وارد کنید'
        })
    )
    Receiver_number = forms.CharField(
        label='شماره تماس ',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '09xxxxxxxxx'
        }))
    Receiver_state = forms.CharField(
        label='استان',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'استان گیرنده را وارد کنید'
        })
    )
    Receiver_city = forms.CharField(
        label='شهر',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شهر گیرنده را وارد کنید'
        })
    )
    receiver_Postal_address = forms.CharField(
        label='ادرس پستی  ',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'ادرس پستی گیرنده را وارد کنید'
        })
    )
    receiver_Postal_code= forms.CharField(
        label='کد پستی  ',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'کد پستی گیرنده بدون - را وارد کنید'
        })
    )