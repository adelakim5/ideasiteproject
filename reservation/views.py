from django.shortcuts import render , redirect, get_object_or_404
from .models import Reservation
from .models import review
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

#def nuovonapoli(request):
    #return render(request, 'nuovonapoli.html')

def index_western(request):
    return render(request, 'index_western.html')

def index_korean(request):
    return render(request, 'index_korean.html')

def index_japanese(request):
    return render(request, 'index_japanese.html')

def index_chinese(request):
    return render(request, 'index_chinese.html')

def western1_nuovonapoli(request):
    return render(request, 'western1_nuovonapoli.html')

def korean1_haemooltang(request):
    return render(request, 'korean1_haemooltang.html')

def korean2_gpoong(request):
    return render(request, 'korean2_gpoong.html')

def japanese1_sbarashi(request):
    return render(request, 'japanese1_sbarashi.html')

def japanese2_gensushi(request):
    return render(request, 'japanese2_gensushi.html')

def chinese1_dhwon(request):
    return render(request, 'chinese1_dhwon.html')

def chinese2_scsung(request):
    return render(request, 'chinese2_scsung.html')

def western2_connys(request):
    return render(request, 'western2_connys.html')

def search_list(request):
    q = request.GET.get('q','')
    if q:
        qs = review.objects.filter(store_name__icontains=q)
        return render(request, 'search.html', {'search_list' : qs ,'q' : q})
    else:
        return render(request, 'search.html')
        
def review_create(request):
    rev = review()
    rev.name = request.POST['name']
    rev.store_name = request.POST['store_name']
    rev.guest_count = request.POST['guest_count']
    rev.pub_date = timezone.datetime.now()
    rev.body = request.POST['body']
    rev.save()

    return redirect('home')

def review_read(request):
    rev = review.objects.all()
    return render(request, 'review.html', {'read_reviews':rev})