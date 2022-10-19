from django.shortcuts import render

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def logaut(request):
    pass

def dashboard(request):
    pass

