from django import template
from jalali_date import datetime2jalali, date2jalali


register = template.Library()

@register.filter(name="show_jalali_date")
def show_jalali_date(value):
    return date2jalali(value)

@register.filter(name="show_jalali_datetime")
def show_jalali_datetime(value):
    return datetime2jalali(value)

@register.filter(name="show_jalali_month")
def show_jalali_month(value):
    months = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
    final_date_format = f'{date2jalali(value).year} - {months[date2jalali(value).month-1]} - {date2jalali(value).day}'
    return final_date_format