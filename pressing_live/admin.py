from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register( Pickup_delivery)
admin.site.register(Client)
admin.site.register(Pressing_blanchisserie)
admin.site.register(Order_service)
admin.site.register(Cloths)
admin.site.register(Price_grid)
admin.site.register(Status)
admin.site.register(Post_offers)
admin.site.register(Order_review)
admin.site.register(Command)
admin.site.register(Command_details)
admin.site.register(Order_info)
admin.site.register(Cloth_info)
admin.site.register(Payement_methode)
admin.site.register(Cash_payement)
admin.site.register(Electronic_payement)
admin.site.register(MTN_money)
admin.site.register(Orange_money)
admin.site.register(Address)
admin.site.register(Localisation)
admin.site.register(Geolocalisation)
admin.site.register(Localisation_ip)
admin.site.register(Service)
admin.site.register(Type)
admin.site.register(Period)