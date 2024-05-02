from django.shortcuts import render
from django import template
import requests

register = template.Library()

@register.filter(name="dollar_price")
def dollar_price(request):
    response = requests.get('http://api.navasan.tech/latest/?api_key=free5FYuj5YLkgVEVOrQVy1CwB6UEdG5').json()
    return render(request,{response:'response'})