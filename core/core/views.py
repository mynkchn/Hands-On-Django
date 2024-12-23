from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request) :
    if request.method=='POST' :
     check=request.POST['check']
     print(check)
    isActive=True
    name="Mayank Chouhan"
    list_of_program=["WAP to check even or odd","WAP to check prime number","WAP to print all prime numbers from 1 to 100","WAP to print pascals triangle"]
    
    student={
        "student_name":"Mayank",
        "student_college":"Parul University",


    }  
    data = {
        'isActive':isActive,
        'name':name,
        'list_of_program':list_of_program,
        'student_data':student,
    }

    return render(request,"home.html",data)
def about(request) :
    return render(request,"about.html",{})
def services(request) :
    return render(request,"services.html",{})