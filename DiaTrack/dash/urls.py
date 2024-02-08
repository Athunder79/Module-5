from django.urls import path
from .views import (
    DashListView, 
    InsulinCreateView, 
    GlucoseCreateView, 
    InsulinChangedCreateView, 
    MealCreateView, 
    ReminderCreateView
)
from . import views

urlpatterns = [
    path('', DashListView.as_view(), name='dash-home'),
    path('detail/',views.detail, name='dash-detail'),
    path('insulin/new/', InsulinCreateView.as_view(), name='insulin-create'),
    path('glucose/new/', GlucoseCreateView.as_view(), name='glucose-create'),
    path('insulin_changed/new/', InsulinChangedCreateView.as_view(), name='insulin_changed-create'),
    path('meal/new/', MealCreateView.as_view(), name='meal-create'),
    path('reminder/new/', ReminderCreateView.as_view(), name='reminder-create'),
    
   
]

