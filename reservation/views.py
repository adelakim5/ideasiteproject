from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def join(request):
    return render(request, 'join.html')

def login(request):
    return render(request, 'login.html')

def nuovonapoli(request):
    return render(request, 'nuovonapoli.html')
