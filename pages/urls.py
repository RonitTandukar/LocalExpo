
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView 
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name="login"),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('thankyou/', views.thankyou, name='contact-success'),
    path('faqs/', views.faqs, name='faqs'),
    path('recommended-shops/', views.recommended_shops, name='recommended-shops'),
    path('quotes/', views.quotes, name='quotes'),
    path('orders/', views.orders, name='orders'),
    path('cart/', views.cart, name='cart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('estimate/', views.estimate, name='estimate'),
    path('editcart/', views.editcart, name='editcart'),
    path('tea/', views.tea, name='products/tea'),
    path('trending/', views.trending, name='trending'),
    path('', views.logout, name='logout'),
    path('buddhastatue/', views.buddhastatue, name="buddhastatue"),
    path('khumbutea/', views.khumbutea, name="khumbutea"),
    path('cg/', views.cg, name="cg"),
    path('carpet/', views.carpet, name="carpet"),
    path('purse/', views.purse, name="purse"),
    path('sahana/', views.sahana, name="sahana"),
    path('st/', views.st, name="st"),
    path('bk1/', views.bk1, name="bk1"),
    path('bk2/', views.bk2, name="bk2"),
    path('bk3/', views.bk3, name="bk3"),
    path('bk4/', views.bk4, name="bk4"),
    path('bk5/', views.bk5, name="bk5"),

]
