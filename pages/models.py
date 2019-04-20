from django.db import models
from datetime import datetime
class UserRegistration(models.Model) :
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = "customer"
    

class ContactUs(models.Model):
    contact_name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Contact"
        db_table = "contact"

class Order(models.Model):
    url = models.CharField(max_length=100)
    quantity = models.CharField(max_length=4)
    comment = models.TextField()
    class Meta:
        db_table = "order"

class Products(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_type = models.CharField(max_length=50)
    Instock = models.CharField(max_length=4)
    Price = models.CharField(max_length=10)
    Product_desc = models.TextField()
    Created_at = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        verbose_name_plural = "Products"
        db_table = "product"

class Vendor(models.Model):
    Name = models.CharField(max_length=50)
    Contact = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Registration_no = models.CharField(max_length=50)
    CitizenShip_no = models.CharField(max_length=50)
    Bank_acc = models.CharField(max_length=50)
    Mailing_address = models.CharField(max_length=50)
    class Meta:
        db_table = "vendor"