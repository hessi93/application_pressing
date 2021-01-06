from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save



class Cloths(models.Model):
    number = models.PositiveIntegerField()
    types = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.CharField(max_length = 30)


class Pickup_delivery(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField()      

class Cash_payement(models.Model):
    total_amount =  models.IntegerField()


class Orange_money(models.Model):
    client_phone =  models.PositiveIntegerField()


class MTN_money(models.Model):
    client_phone =  models.PositiveIntegerField()


class Electronic_payement(models.Model):
    orange_money = models.ForeignKey(Orange_money, on_delete = models.CASCADE)
    mtn_money = models.ForeignKey(MTN_money, on_delete = models.CASCADE)

class  Payement_methode(models.Model):
    cash_payement = models.ForeignKey(Cash_payement, on_delete = models.CASCADE)
    electronic_payement = models.ForeignKey(Electronic_payement, on_delete = models.CASCADE)


class Order_info(models.Model):
    payement_methode = models.OneToOneField(Payement_methode,on_delete=models.CASCADE)
    pickup_delivery = models.OneToOneField(Pickup_delivery,on_delete=models.CASCADE)


class Order_review(models.Model):
    payeble_amount = models.IntegerField(null=True)
    transport_fee = models.IntegerField()


class Address(models.Model): 
    city = models.CharField(max_length=30)
    quater = models.CharField(max_length=30)
    description = models.TextField()
    order_info = models.ForeignKey(Order_info, on_delete = models.CASCADE)


class Order_service(models.Model):
    date = models.DateField(auto_now_add=True)
    total = models.IntegerField()
    Service_provider = models.CharField(max_length=30)
    cloths = models.ForeignKey(Cloths, on_delete = models.CASCADE)
    pickup_delivery = models.OneToOneField(Pickup_delivery,on_delete=models.CASCADE)
    order_review = models.OneToOneField(Order_review,on_delete=models.CASCADE)
    payement_methode = models.OneToOneField(Payement_methode,on_delete=models.CASCADE)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)


class Status(models.Model):
    processing = models.BooleanField(default=False,null=True)
    readytodeliver = models.BooleanField(default=False,null=True)
    on_hold = models.BooleanField(default=False,null=True)


class Price_grid(models.Model):
     cloths = models.OneToOneField(Cloths,on_delete=models.CASCADE)


class Command_details(models.Model):
    client_name = models.CharField(max_length=20)
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    order_info = models.ForeignKey(Order_info, on_delete = models.CASCADE,related_name ='orders_info')
    cloth_info = models.ForeignKey(Order_info, on_delete = models.CASCADE,related_name ='cloths_info')

class Command(models.Model):
    received_date = models.DateField()
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    command_details = models.OneToOneField(Command_details,on_delete=models.CASCADE) 
    order_service = models.OneToOneField(Order_service,on_delete=models.CASCADE) 


class Period(models.Model):
    starting_date = models.DateField()
    ending_date = models.DateField()


class Post_offers(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='image/')
    period = models.OneToOneField(Period,on_delete=models.CASCADE)


class Pressing_blanchisserie(models.Model):
    name = models.CharField(max_length =30)
    email = models.TextField(max_length = 20)
    password = models.CharField(max_length =20)
    telephone = models.PositiveIntegerField()
    social_raison =models.TextField(max_length=30)
    price_grid = models.OneToOneField(Price_grid,on_delete=models.CASCADE)
    commend = models.ForeignKey(Command, on_delete = models.CASCADE)
    post_offers = models.ForeignKey(Post_offers, on_delete = models.CASCADE)



class Client(models.Model):
    name = models.CharField(max_length =30)
    email = models.TextField(max_length = 20)
    password = models.CharField(max_length =20)
    telephone = models.PositiveIntegerField()
    order_service = models.ForeignKey(Order_service, on_delete = models.CASCADE)
    pressing_blanchisserie = models.OneToOneField(Pressing_blanchisserie,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Cloth_info(models.Model):
    mark = models.CharField(max_length=20)
    color = models.CharField(max_length=10)


class Geolocalisation(models.Model):
    longitude = models.DecimalField( max_digits=5, decimal_places=2)          
    latitude = models.DecimalField( max_digits=5, decimal_places=2)

class Localisation_ip(models.Model):
    ip_adress = models.DecimalField( max_digits=5, decimal_places=2)

class Localisation(models.Model):
    geolocalisation = models.ForeignKey(Geolocalisation, on_delete = models.CASCADE)      
    localisation_ip = models.ForeignKey(Localisation_ip, on_delete = models.CASCADE)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)


class Type(models.Model):
    price = models.IntegerField()
    service_time = models.TimeField()
    #classic = models.ForeignKey(Classic, on_delete = models.CASCADE)
    #express = models.ForeignKey(Express, on_delete = models.CASCADE)
    #at_home = models.ForeignKey(At_home, on_delete = models.CASCADE)


class Service(models.Model):
    type = models.OneToOneField(Type,on_delete=models.CASCADE)
    service_time = models.TimeField() 
    client = models.OneToOneField(Client,on_delete=models.CASCADE)


                   