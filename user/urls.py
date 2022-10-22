"""social_welfare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('societies/',views.societies,name="societies"),
    path('societies_oldage/',views.societies_oldage,name="societies_oldage"),
    path('societies_oldage_member/<int:pk>/',views.societies_oldage_member,name="societies_oldage_member"),
    path('societies_oldage_donate/<int:pk>/',views.societies_oldage_donate,name="societies_oldage_donate"),
    path('societies_women/',views.societies_women,name="societies_women"),
    path('societies_women_member/<int:pk>/',views.societies_women_member,name="societies_women_member"),
    path('societies_women_donate/<int:pk>/',views.societies_women_donate,name="societies_women_donate"),
    path('societies_orphanage/',views.societies_orphanage,name="societies_orphanage"),
    path('societies_orphanage_member/<int:pk>/',views.societies_orphanage_member,name="societies_orphanage_member"),
    path('societies_orphanage_donate/<int:pk>/',views.societies_orphanage_donate,name="societies_orphanage_donate"),
    path('adoption/',views.adoption,name="adoption"),
    path('adoption_members/',views.adoption_members,name="adoption_members"),
    path('adoption_member_detail/<int:pk>/',views.adoption_member_detail,name="adoption_member_detail"),
    path('adoption_member_adopt/<int:pk>/',views.adoption_member_adopt,name="adoption_member_adopt"),
    path('sponsorship/',views.sponsorship,name="sponsorship"),
    path('sponsorship_members/',views.sponsorship_members,name="sponsorship_members"),
    path('sponsorship_member_detail/<int:pk>/',views.sponsorship_member_detail,name="sponsorship_member_detail"),
    path('sponsorship_member_sponsor/<int:pk>/',views.sponsorship_member_sponsor,name="sponsorship_member_sponsor"),
    path('wedding/',views.wedding,name="wedding"),
    path('wedding_welfares/',views.wedding_welfares,name="wedding_welfares"),

    path('wedding_member_detail/<int:pk>/',views.wedding_member_detail,name="wedding_member_detail"),
    path('wedding_member_propose/<int:pk>/',views.wedding_member_propose,name="wedding_member_propose"),
    path('purchase/',views.purchase,name="purchase"),
    path('purchase_buy/<int:pk>/',views.purchase_buy,name="purchase_buy"),
    path('purchase_orphanage/',views.purchase_orphanage,name="purchase_orphanage"),
    path('purchase_orphanage_buy/<int:pk>/',views.purchase_orphanage_buy,name="purchase_orphanage_buy"),

    path('viewaddjob/',views.viewaddjob,name="viewaddjob"),

    path('addjob',views.addjob,name="addjob"),
    
]
