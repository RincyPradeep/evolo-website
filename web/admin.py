from django.contrib import admin
from web.models import Customer,Service,Feature,Pricing,Contact,Video,Team


admin.site.register(Customer)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","description"]

admin.site.register(Service,ServiceAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","description","list_items"]

admin.site.register(Feature,FeatureAdmin)


class PricingAdmin(admin.ModelAdmin):
    list_display = ["id","title","description","price_in_dollar","feature_list","not_feature_list"]

admin.site.register(Pricing,PricingAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["id","full_name","email","phone","interested_in","user_agreement"]

admin.site.register(Contact,ContactAdmin)


admin.site.register(Video)


class TeamAdmin(admin.ModelAdmin):
    list_display = ["id","name","image","designation"]

admin.site.register(Team,TeamAdmin)