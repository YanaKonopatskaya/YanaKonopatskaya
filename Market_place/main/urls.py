
from django.urls import path, include
from .views import *
app_name='main'
urlpatterns = [
    path('',start_page,name='start_page'),
]
