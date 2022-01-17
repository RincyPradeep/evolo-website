from django.shortcuts import render
from web.models import Customer


def index(request):
    customers = Customer.objects.all()

    context={
        "customers" : customers
    }
    
    return render(request,"index.html",context=context)
