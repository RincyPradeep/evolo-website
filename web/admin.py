from django.contrib import admin
from web.models import Customer,Service,Feature,Pricing


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