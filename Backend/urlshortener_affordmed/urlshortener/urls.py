from django.urls import path
from .views import shorten_url, redirect_url
#this code is for URL routing in the URL shortener application



#routing is declared here for the URL shortener application

urlpatterns = [
    path('shorten/', shorten_url, name='shorten'),
    path('<str:code>/', redirect_url, name='redirect'),
]
