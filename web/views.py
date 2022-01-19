from django.shortcuts import render
from web.models import Customer,Service,Feature,Pricing


def index(request):
    customers = Customer.objects.all()
    services = Service.objects.all()
    features = Feature.objects.all()
    pricings = Pricing.objects.all()

    context={
        "customers" : customers,
        "services" : services,
        "features" : features,
        "pricings" : pricings
    }
    
    return render(request,"index.html",context=context)
