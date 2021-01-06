from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#from django.forms import *
from .models import *



class CreateUserForm(UserCreationForm):
    
    class Meta : 
        model = User
        fields = ['first_name','last_name','email','username','password1', 'password2',]



class Clientform(ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')


class Pressing_blanchisserieform(ModelForm):
    class Meta:
        model = Pressing_blanchisserie
        fields = ('__all__') 


class Order_serviceform(ModelForm):
    class Meta:
        model = Order_service
        fields = ('__all__') 


class Clothsform(ModelForm):
    class Meta:
        model = Cloths
        fields = ('__all__') 


class Price_gridform(ModelForm):
    class Meta:
        model = Price_grid
        fields = ('__all__')


class Statusform(ModelForm):
    class Meta:
        model = Status
        fields = ('__all__')


class Post_offersform(ModelForm):
    class Meta:
        model = Post_offers
        fields = ('__all__')


class pickup_deliveryform(ModelForm):
    class Meta:
        model = Pickup_delivery
        fields = ('__all__')


class Order_reviewform(ModelForm):
    class Meta:
        model = Order_review
        fields = ('__all__')


class Commandform(ModelForm):
    class Meta:
        model = Command
        fields = ('__all__')


class Command_detailsform(ModelForm):
    class Meta:
        model = Command_details
        fields = ('__all__')


class Order_infoform(ModelForm):
    class Meta:
        model = Order_info
        fields = ('__all__')


class Cloth_infoform(ModelForm):
    class Meta:
        model = Cloth_info
        fields = ('__all__')


class Payement_methodeform(ModelForm):
    class Meta:
        model = Payement_methode
        fields = ('__all__')



class Cash_payementform(ModelForm):
    class Meta:
        model = Cash_payement
        fields = ('__all__')


class Electronic_payementform(ModelForm):
    class Meta:
        model = Electronic_payement
        fields = ('__all__') 


class MTN_moneyform(ModelForm):
    class Meta:
        model = MTN_money
        fields = ('__all__')


class Orange_moneyform(ModelForm):
    class Meta:
        model = Orange_money
        fields = ('__all__')


class Addressform(ModelForm):
    class Meta:
        model = Address
        fields = ('__all__') 



class Localisationform(ModelForm):
    class Meta:
        model = Localisation
        fields = ('__all__')


class Geolocalisationform(ModelForm):
    class Meta:
        model = Geolocalisation
        fields = ('__all__')


class Localisation_ipform(ModelForm):
    class Meta:
        model = Localisation_ip
        fields = ('__all__')



class Serviceform(ModelForm):
    class Meta:
        model = Service
        fields = ('__all__') 


class Typeform(ModelForm):
    class Meta:
        model = Type
        fields = ('__all__')


class Periodform(ModelForm):
    class Meta:
        model = Period
        fields = ('__all__')
