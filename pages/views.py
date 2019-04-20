# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pages.forms import UserRegistrationForm, ContactUsForm, OrderForm
from pages.models import UserRegistration, ContactUs, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.template import RequestContext
from django.db import connection


def index(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = OrderForm

    return render(request, "index.html", {'form': form})


def about(request):
    return render(request, "about.html", {})


def tea(request):
    return render(request, "products/tea.html", {})


def login(request):

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        return redirect('cart')

    return render(request, 'login.html', {})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        print(form)
        if(form.is_valid):
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm

    return render(request, 'register.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('index.html')


def thankyou(request):
    return render(request, 'thankyou.html', {})


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('contact-success')
    else:
        form = ContactUsForm

    return render(request, 'contact.html', {'form': form})


def faqs(request):
    return render(request, 'faqs.html', {})


def recommended_shops(request):
    return render(request, 'recommendedshops.html', {})


def dashboard(request):
    showitems = Order.objects.all()
    customers = UserRegistration.objects.all()
    return render(request, 'dashboard.html', {'showitems': showitems ,'customers': customers})

def quotes(request):
    return render(request, 'quotes.html', {})


def orders(request):
    return render(request, 'orders.html', {})


def cart(request):
    showitems = Order.objects.all()
    return render(request, 'cart.html', {'showitems': showitems})
    


def estimate(request):
    return render(request, 'estimate.html', {})

def tea(request):
    return render(request, 'products/tea.html', {})

# def products_handicrafts(request):
#    return render(request, 'products/handicrafts.html', {})

def editcart(request):
    return render(request, 'editcart.html', {})

def trending(request):
    return render(request, 'trending.html', {})

def buddhastatue(request):
    return render(request, 'buddhastatue.html', {})
    
def estimate(request):
    return render(request, 'estimate.html', {})

def khumbutea(request):
    return render(request, 'khumbutea.html', {})

def carpet(request):
    return render(request, 'carpet.html', {})

def cg(request):
    return render(request, 'cg.html', {})
    
def purse(request):
    return render(request, 'purse.html', {})

def sahana(request):
    return render(request, 'sahana.html', {})

def st(request):
    return render(request, 'st.html', {})

def vajra(request):
    return render(request, 'vajra.html', {})

def bk1(request):
    return render(request, 'bk1.html', {})

def bk2(request):
    return render(request, 'bk2.html', {})

def bk3(request):
    return render(request, 'bk3.html', {})

def bk4(request):
    return render(request, 'bk4.html', {})

def bk5(request):
    return render(request, 'bk5.html', {})

def logout(request):
    return render(request, 'index.html', {})