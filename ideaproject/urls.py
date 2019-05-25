"""ideaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservation import views as reservation
import reservation.views
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reservation.views.home, name="home"),
    #path('index', reservation.views.index, name="index"),
    path('accounts/signup/', accounts.signup, name='signup'),
    path('accounts/login/', accounts.login, name='login'),
    path('accounts/logout/', accounts.logout, name='logout'),
    #path('nuovonapoli/', reservation.views.nuovonapoli, name="nuovonapoli"),
    path('index_western/', reservation.views.index_western, name="index_western"),
    path('index_japanese/', reservation.views.index_japanese, name="index_japanese"),
    path('index_chinese/', reservation.views.index_chinese, name="index_chinese"),
    path('index_korean/', reservation.views.index_korean, name="index_korean"),
    path('index_western/western1_nuovonapoli/', reservation.views.western1_nuovonapoli, name="western1_nuovonapoli"),
    path('index_western/western2_connys/', reservation.views.western2_connys, name="western2_connys"),
    path('index_korean/korean1_haemooltang/', reservation.views.korean1_haemooltang, name="korean1_haemooltang"),
    path('index_korean/korean2_gpoong/', reservation.views.korean2_gpoong, name="korean2_gpoong"),
    path('index_japanese/japanese1_sbarashi/', reservation.views.japanese1_sbarashi, name="japanese1_sbarashi"),
    path('index_japanese/japanese2_gensushi/', reservation.views.japanese2_gensushi, name="japanese2_gensushi"),
    path('index_chinese/chinese1_dhwon/', reservation.views.chinese1_dhwon, name="chinese1_dhwon"),
    path('index_chinese/chinese2_scsung/', reservation.views.chinese2_scsung, name="chinese2_scsung"),
    # path('accounts/', include('accounts.urls')),
    path('search/', reservation.views.search_list, name="search"),
    path('review_create/', reservation.views.review_create, name="review_create"),
    path('review_read/', reservation.views.review_read, name="review_read"),
]