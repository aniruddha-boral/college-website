from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
class Admission(models.Model):
    fname=models.TextField()
    lname=models.TextField()
    email=models.TextField()
    gender=models.TextField()
    phone=models.TextField()
    gname=models.TextField()
    gphone=models.TextField()
    address=models.TextField()
    sec=models.TextField()
    hsec=models.TextField()
    wbjee=models.TextField()
    
