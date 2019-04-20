from django import forms
from pages.models import UserRegistration
from pages.models import ContactUs
from pages.models import Order
from pages.models import Products
from pages.models import Vendor

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"