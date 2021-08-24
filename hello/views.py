from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Admission


# Create your views here.

def home(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "home.html")
def about(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "about.html")
def faculty(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "faculty.html")
def campus(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "campus.html")
def facility(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "facility.html")
def placement(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "placement.html")
def contact(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "contact.html")
def admission(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "admission.html")
def enquiry(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "enquiry.html")
def table(request):
    lp = Admission.objects.all()
    lq = Admission.objects.filter().count()
    lr = Admission.objects.filter(gender='m').count()
    ls = Admission.objects.filter(gender='f').count()
    # return HttpResponse('Hello from Python!')
    return render(request,"table.html",{"lp":lp,"lq":lq,"lr":lr,"ls":ls})
def admission_hid(request):
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    email=request.POST.get("email")
    gender=request.POST.get("gender")
    phone=request.POST.get("phone")
    gname=request.POST.get("gname")
    gphone=request.POST.get("gphone")
    address=request.POST.get("address")
    sec=request.POST.get("sec")
    hsec=request.POST.get("hsec")
    wbjee=request.POST.get("wbjee")
    

    obj=Admission()
    obj.fname=fname
    obj.lname=lname
    obj.email=email
    obj.gender=gender
    obj.phone=phone
    obj.gname=gname
    obj.gphone=gphone
    obj.address=address
    obj.sec=sec
    obj.hsec=hsec
    obj.wbjee=wbjee
    

    obj.save()
    

    # return HttpResponse('Hello from Python!')
    return render(request, "admission_hid.html",{"fname":fname, "lname":lname, "email":email, "gender":gender, "phone":phone, "gname":gname, "gphone":gphone, "address":address, "sec":sec, "hsec":hsec, "wbjee":wbjee})

def delete(request):
    did=request.POST.get("did")
    

    pdel=Admission.objects.filter(id=did).delete()
    

    return render(request, "delete.html",{"did":did})

def base(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "base.html")
def lc(request):
    un=request.POST.get("un")
    pas=request.POST.get("pas")
    


    # return HttpResponse('Hello from Python!')
    return render(request, "lc.html",{"un":un, "pas":pas})

def logout(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "logout.html")

def navbar(request):
    return render(request, "navbar.html")

def student(request):
    return render(request, "student.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

