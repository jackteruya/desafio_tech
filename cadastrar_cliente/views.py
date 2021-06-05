from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from cadastrar_cliente.models import Customer
from django.template import Context, loader


@login_required(login_url="/login/")
def register_customer(request):
    return render(request, 'register-customer.html')

@login_required(login_url="/login/")
def set_customer(request):
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    customers = Customer.objects.create(cpf=cpf, email=email)

    url = '/customer/detail/{}/'.format(customers.id)
    return redirect(url)

@login_required(login_url="/login/")
def delete_customer(request, id):
    customers = Customer.objects.get(id=id)
    if customers.user == request.user:
        customers.delete()
    return redirect('/')

@login_required(login_url='/login/')
def liste_all_customer(request):
    customers = Customer.objects.all()
    return render(request, 'list.html', {'customers':customers})

def customer_detail(request, id):
    customers = Customer.objects.get(id=id)
    return render(request, 'customer.html', {'customers':customers})

def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usário e senha inválida. Favor tentar novamente.')
    return redirect('/login/')
