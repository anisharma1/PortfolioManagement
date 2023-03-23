"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #Include default auth urls.
    path('', include('django.contrib.auth.urls')),

    #My Page
    path('register/', views.register, name='register'),

    # redirects to logout page
    path('logout/', views.logout, name='logout'),

    
    # path('stockadded/<int:slug>',views.addstocks,name='addstocks'),
    # path('stockdeleted/<int:slug>',views.deletestocks,name='deletestocks'),

    # redirects to all stocks profiles page
    path('stockprofiles/', views.stockprofiles, name='stockprofiles'),

    # redirects to all dashboard 
    path('dashboard/', views.dashboard, name='dashboard'),

    # redirects to all stocks page 
    path('stocks/', views.stocks, name='stocks'),
    
]
