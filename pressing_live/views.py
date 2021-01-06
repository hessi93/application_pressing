from django.shortcuts import render, redirect


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from . models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,'home.html')


def command(request):
    return render(request,'command.html')


def command_details(request):
    return render(request,'command_details.html')


def order_info(request):
    return render(request,'order_info.html')
    
def cloth_info(request):
    return render(request,'cloth_info.html')


def status(request):
    return render(request,'status.html')


    
def order_service(request):
    return render(request,'order_service.html')


def order_review(request):
    return render(request,'Order_review.html')


def pickup_delivery(request):
    return render(request,'pickup_delivery.html')


def payement_methode(request):
    return render(request,'payement_methode.html')


def cash_payement(request):
    return render(request,'cash_payement.html')


def electronic_payement(request):
    return render(request,'electronic_payement.html')


def orange_money(request):
    return render(request,'orange_money.html')


def MTN_money(request):
    return render(request,'MTN_money.html')


def address(request):
    return render(request,'address.html')


def cloths(request):
    return render(request,'cloths.html')


def price_grid(request):
    return render(request,'price_grid.html')


def post_offers(request):
    return render(request,'post_offers.html')


def period(request):
    return render(request,'period.html')


def localisation(request):
    return render(request,'localisation.html')


def geolocalisation(request):
    return render(request,'geolocalisation.html')


def localisation_ip(request):
    return render(request,'localisation_ip.html')


def service(request):
    return render(request,'service.html')


def type(request):
    return render(request,'type.html')


def pressing_blanchisserie(request):
    return render(request,'pressing_blanchisserie.html')





def registerPage(request):
    # if request.user.is_authenticated:
    #         return redirect('login')  
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'ivy was created for' + user)
            return redirect('login')
        else:
            print('essai')
            print(form.errors)
    
            return redirect('register')

    context = {'form':form }
    return render(request, 'authentification/register.html', context)



def loginPage(request):
    if request.user.is_authenticated:
         return redirect('home') 
    else:   
        print('verification')
        if request.method == 'POST':
            print(request.method)
            username = request.POST.get('username')
            password = request.POST.get('password')
            print (username) 
            print (password) 
            
            user = authenticate(request, username=username, password=password)
            print(user)
            
            if user is not None:
                login(request, user)
                return render(request, "home.html")
            else:
                messages.info(request, 'username OR password is incorrect')    
                return render(request, 'authentification/login.html')
        else:
            context = {}
            print('authentification/login.html')
            return render(request, 'authentification/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')