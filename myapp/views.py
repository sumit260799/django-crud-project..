from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index (request):
    return render(request,'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'view_emp.html',context)
def add_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        date= request.POST.get('date')
        data = Employee(name=name,location=location,age = age,salary=salary,date=date)

        data.save()    

    return render(request,'add_emp.html')
# def add_emp(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         location = request.POST.get('location')
#         age = request.POST.get('age')
#         date = request.POST.get('date')
#         contact = Employee(name = name,location = location ,age = age,date=date)
#         contact.save()
#         messages.success(request, 'your message has been sent!')
     
        
    

#     return render(request, "add_emp.html")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("emp removed successfully!")
        
            
            
        except:
            return HttpResponse("choose correct id")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    
    return render(request,'remove_emp.html',context)
def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(name__icontains = name)
        if age:
            emps = emps.filter(age=age)
        context={
            'emps':emps
            }
        return render (request,'view_emp.html',context)
    elif request.method == "GET":
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('an exception occured!')