from django.shortcuts import render
from .models import ContactUs
def contact(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        email = request.POST.get("item3")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        created = ''
        read_by_admin = None
        admin_response= ''
        listall = ContactUs(subject=subject,message=message,full_name=full_name,email=email,phone=phone,created=created,read_by_admin=read_by_admin,
                            admin_response=admin_response)
        listall.save()
        return render(request,'contact/index.html')
    return render(request,'contact/index.html')
