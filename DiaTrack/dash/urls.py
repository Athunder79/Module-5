from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dash-home'),
    path('detail/',views.detail, name='dash-detail'),
   
]