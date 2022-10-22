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
    path('admin_home/',views.index,name="index"),
    path('',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('view_society/',views.view_society,name="view_society"),
    path('active_society/<int:pk>/',views.active_society,name="active_society"),
    path('remove_society/<int:pk>/',views.remove_society,name="remove_society"),
    # path('view_oldage/',views.view_oldage,name="view_oldage"),
    # path('active_oldage/<int:pk>/',views.active_oldage,name="active_oldage"),
    # path('remove_oldage/<int:pk>/',views.remove_oldage,name="remove_oldage"),
    # path('view_women_welfare/',views.view_women_welfare,name="view_women_welfare"),
    # path('active_women_welfare/<int:pk>/',views.active_women_welfare,name="active_women_welfare"),
    # path('remove_women_welfare/<int:pk>/',views.remove_women_welfare,name="remove_women_welfare"),
    path('view_welfares/',views.view_welfares,name="view_welfares"),
    path('view_welfares_oldage/',views.view_welfares_oldage,name="view_welfares_oldage"),
    path('view_oldage_members/<int:pk>/',views.view_oldage_members,name="view_oldage_members"),
    path('view_welfares_women/',views.view_welfares_women,name="view_welfares_women"),
    path('view_women_members/<int:pk>/',views.view_women_members,name="view_women_members"),
    path('view_welfare_orphanage/',views.view_welfare_orphanage,name="view_welfare_orphanage"),
    path('view_orphanage_members/<int:pk>/',views.view_orphanage_members,name="view_orphanage_members"),
    path('view_products/',views.view_products,name="view_products"),
    path('view_purchase/',views.view_purchase,name="view_purchase"),
    path('view_marriage_details/',views.view_marriage_details,name="view_marriage_details"),
    path('view_donation/',views.view_donation,name="view_donation"),

    path('approvejob/',views.approvejob,name="approvejob"),

    path('approvedjobs/<int:pk>/',views.approvedjobs,name="approvedjobs"),

    path('showjob',views.showjob,name="showjob"),

    path('showjobof',views.showjobof,name="showjobof"),

    path('removejob/<int:pk>/',views.removejob,name="removejob"),


]
