from django.urls import path
from . import views

urlpatterns = [
    path('',views.oldage_home,name="oldage_home"),
    path('view_members/',views.view_members,name="view_members"),   
    path('add_members/',views.add_members,name="add_members"),    
    path('edit_members/<int:pk>/',views.edit_members,name="edit_members"),    
    path('edit_member_details/<int:pk>/',views.edit_member_details,name="edit_member_details"),    
    path('delete_member/<int:pk>/',views.delete_member,name="delete_member"),    
    path('view_donation/',views.view_donation,name="view_donation"),    
    path('receive/<int:pk>/',views.receive,name="receive"),    
]
