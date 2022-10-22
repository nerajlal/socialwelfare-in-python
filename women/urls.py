from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('view_members/',views.view_members,name="view_members"),
    path('add_members/',views.add_members,name="add_members"),
    path('edit_members/<int:pk>/',views.edit_members,name="edit_members"),
    path('delete_members/<int:pk>/',views.delete_members,name="delete_members"),
    path('proposals/',views.proposals,name="proposals"),
    path('products/',views.products,name="products"),
    path('add_products/',views.add_products,name="add_products"),
    path('edit_products/<int:pk>/',views.edit_products,name="edit_products"),
    path('delete_products/<int:pk>/',views.delete_products,name="delete_products"),
    path('purchase/',views.purchase,name="purchase"),
    path('donations/',views.donations,name="donations"),
    path('donation_received/<int:pk>/',views.donation_received,name="donation_received"),

    path('showjob/',views.showjob,name="showjob"),
    
]