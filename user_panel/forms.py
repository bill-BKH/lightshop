from django import forms
<<<<<<< HEAD
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
=======
from account.models import User

class PersonalForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'phone', 'id_number', 'cart_number']
        labels = {
            'name': 'نام  ‍',
            'last_name':'خانوادگی',
            'phone': 'شماره تماس',
            'email': 'ایمیل',
            'id_number': 'کد ملی',
            'cart_number': 'شماره کارت ',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'phone': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'id_number': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'cart_number': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'email':forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        })
        }
>>>>>>> a6c731b (commit message)
