from django.urls import path
from . import views
from .views import DashListView, InsulinCreateView

urlpatterns = [
    path('', DashListView.as_view(), name='dash-home'),
    path('detail/',views.detail, name='dash-detail'),
    path('insulin/new/', InsulinCreateView.as_view(), name='insulin-create'),
    
   
]

