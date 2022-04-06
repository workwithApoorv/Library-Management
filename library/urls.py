from django import views
from django.contrib import admin
from django.urls import path, include
from .views import home,add,signup,user_login,user_logout,update_book,delete_object,list_book

urlpatterns = [
    path('home', home, name="Home"),
    path('add_user_book', add, name='add'),
    path('signup',signup,name='signup'),
    path('login',user_login,name='login'),
    path('logout',user_logout,name='logout'),
    path('update',update_book,name='update'),
    path('delete',delete_object,name='delete'),
    path('list',list_book,name='list')

]
