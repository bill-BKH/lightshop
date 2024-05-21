from django import forms

class Product_Comment_Form(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'input-ui pr-2 pt-2 my_comment',
            
        }))
