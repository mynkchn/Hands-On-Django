from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def home(request) :
    details=Emp.objects.all()
    return render(request,'emp/home.html',{'details':details})
    

def add_emp(request) :

    if request.method=='POST' :
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        working=request.POST.get('working')
        course=request.POST.get('course')
        e=Emp()
        e.name=name
        e.email=email
        e.phone=phone
        e.address=address
        e.working=working
        if e.working is None :
         e.working=False
        else :
         e.working=True   
        e.course=course   
        e.save() 
        return redirect('/emp/home')
    return render(request,'emp/add_emp.html',{})

def delete(request,emp_id) : 
   emp=Emp.objects.get(pk=emp_id)
   emp.delete()
   return redirect('/emp/home')

def update(request,emp_id) :
   emp=Emp.objects.get(pk=emp_id)
   

def testinomial(request) :
   testi=Testimonial.objects.all()
   return render(request,'emp/testinomial.html',{'testi':testi})
