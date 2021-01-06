from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'), 
    path('pressing_blanchisserie/', views.pressing_blanchisserie, name = 'pressing_blanchisserie'),
    path('command/', views.command, name = 'command'),
    path('command_details/', views.command_details, name = 'command_details'),
    path('order_info/', views.order_info, name = 'order_info'),
    path('cloth_info/', views.cloth_info, name = 'cloth_info'),
    path('status/', views.status, name = 'status'),
    path('order_service/', views.order_service, name = 'order_service'),
    path('order_review/', views.order_review, name = 'order_review'),
    path('pickup_delivery/', views.pickup_delivery, name = 'pickup_delivery'),
    path('payement_methode/', views.Payement_methode, name = 'payement_methode'),
    path('cash_payement/', views.cash_payement, name = 'cash_payement'),
    path('electronic_payement/', views.electronic_payement, name = 'electronic_payement'),
    path('orange_money/', views.orange_money, name = 'orange_money'),
    path('MTN_money/', views.MTN_money, name = 'MTN_money'),
    path('address', views.address, name = 'address'),
    path('cloths/', views.cloths, name = 'cloths'),
    path('price_grid/', views.price_grid, name = 'price_grid'),
    path('post_offers/', views.post_offers, name = 'post_offers'),
    path('period/', views.period, name = 'period'),
    path('localisation/', views.localisation, name = 'localisation'),
    path('geolocalisation/', views.geolocalisation, name = 'geolocalisation'),
    path('localisation_ip/', views.localisation_ip, name = 'localisation_ip'),
    path('service', views.service, name = 'service'),
    path('type/', views.type, name = 'type'),
    
]