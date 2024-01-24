from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dash-home'),
    path('page2/', views.page2, name='dash-page2'),
]