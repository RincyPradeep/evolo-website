import json
from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Customer,Service,Feature,Pricing,Contact,Video,Team
from web.forms import ContactForm


def index(request):
    customers = Customer.objects.all()
    services = Service.objects.all()
    features = Feature.objects.all()
    pricings = Pricing.objects.all()
    videos = Video.objects.all()[:1]
    team_members = Team.objects.all()

    form = ContactForm()

    context={
        "customers" : customers,
        "services" : services,
        "features" : features,
        "pricings" : pricings,
        "form" : form,
        "videos" : videos,
        "team_members" : team_members
    }
    
    return render(request,"index.html",context=context)


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        
        email = request.POST.get("email")

        if not Contact.objects.filter(email=email).exists():
            form.save()
            response_data = {
                "status" : "success",
                "title" : "Successfully Registered",
                "message" : "You subscribed to our newsletter successfully"
            }
        else:
            response_data = {
                "status" : "error",
                "title" : "You are already registered",
                "message" : "You are already a member. No need to register again."
            }
    else:
        response_data = {
            "status" : "error",
            "title" : "Invalid data",
            "message" : "Please enter valid data."
        }

    return HttpResponse(json.dumps(response_data), content_type = "application/javascript")
