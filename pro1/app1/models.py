from django.db import models
from django.core import validators

# Create your models here.
class Client(models.Model):
    s= [("Onboarded","Onboarded",),("Not Onboarded","Not Onboarded")]
    d = [("SAAS","SAAS"),("Ecommerce","Ecommerce"),("CRM","CRM"),("ERP","ERP"),("Finance","Finance")]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False , blank=False)
    company = models.CharField(max_length=50, null=False , blank=False)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50, null=False,blank=False)
    date_of_joining = models.DateField()
    status = models.CharField(max_length=23,choices=s)
    project_Domain = models.CharField(max_length=23,choices=d)