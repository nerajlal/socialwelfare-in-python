from django.urls import path
from . import views

urlpatterns = [
    path('',views.orphanage_home,name="orphanage_home"),
    path('view_members/',views.view_members,name="view_members"),    
    path('add_members/',views.add_members,name="add_members"),    
    path('edit_member/<int:pk>/',views.edit_member,name="edit_member"),    
    path('edit_member1/<int:pk>/',views.edit_member1,name="edit_member1"),    
    path('delete_member/<int:pk>/',views.delete_member,name="delete_member"),    
    path('view_products/',views.view_products,name="view_products"),    
    path('add_products/',views.add_products,name="add_products"),   
     path('edit_product/<int:pk>/',views.edit_product,name="edit_product"),    
    path('edit_product1/<int:pk>/',views.edit_product1,name="edit_product1"),  
    path('delete_product/<int:pk>/',views.delete_product,name="delete_product"),  
    path('view_purchase/',views.view_purchase,name="view_purchase"),  
    path('view_adoption/',views.view_adoption,name="view_adoption"),  
    path('view_sponsor/',views.view_sponsor,name="view_sponsor"),  
    path('view_donation/',views.view_donation,name="view_donation"),  
    path('receive/<int:pk>/',views.receive,name="receive"),  
    path('showjob',views.showjob,name="showjob"),
]
