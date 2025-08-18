from django.urls import path
from . import views

urlpatterns = [
    path('', views.auction_home, name='auction_home'),
]