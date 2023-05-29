from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render,redirect
from django.core import paginator
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import empdata
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

@login_required(login_url='/loginpage/')
#creating views for homepage,loginpage,empform,empdetails
def homepage(request):
    return render(request,'homepage.html')

def loginpage(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else: #login authentication
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('homepage')
        else:
            messages.success(request,'Invalid details!')
            return render(request, 'login.html')

#creating logout view 
def logoutpage(request):
    logout(request)
    return redirect('loginpage') 

def empform(request):
    if request.method == 'GET':
        empdat = empdata.objects.all().values()
        last_employee = empdata.objects.last()
        last_employee_id = last_employee.empid if last_employee else 0
        context = {
            'last_employee_id': last_employee_id,
            'empdat': empdat
        }
        return render(request, 'empform.html', context)
    else:
        empdata(
            empid=request.POST.get('eid'),
            empname=request.POST.get('ename'),
            doj=request.POST.get('doj'),
            expsalary=request.POST.get('esal'),
            prevexp=request.POST.get('prevexp'),
            designation=request.POST.get('desg')
        ).save()
        messages.success(request, 'Form submitted successfully.')
        empdat = empdata.objects.all().values()
        last_employee = empdata.objects.last()
        last_employee_id = last_employee.empid if last_employee else 0
        context = {
            'last_employee_id': last_employee_id,
            'empdat': empdat
        }
        return render(request, 'empform.html', context)




from django.shortcuts import redirect

def empdetails(request):
    if request.method == 'GET':
        empdat = empdata.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(empdat, 5)
        try:
            empdat = paginator.page(page)
        except PageNotAnInteger:
            empdat = paginator.page(1)
        except EmptyPage:
            empdat = paginator.page(paginator.num_pages)
        sortedUrl = "http://localhost:8000/employees/?s_flag=asc"
        return render(request, 'empdetails.html', {'empdat': empdat})
    else:
        action = request.POST.get('action')  # Get the action parameter from the form
        
        if action == 'create':
            empdata(
                empid=request.POST.get('eid'),
                empname=request.POST.get('ename'),
                doj=request.POST.get('doj'),
                expsalary=request.POST.get('esal'),
                prevexp=request.POST.get('prevexp'),
                designation=request.POST.get('desg')
            ).save()
        
        return redirect('empdetails')  # Redirect to the empdetails view after the operation



