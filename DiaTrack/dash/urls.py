from django.urls import path
from .views import (
    DashListView, 
    InsulinCreateView, 
    GlucoseCreateView, 
    InsulinChangedCreateView, 
    MealCreateView, 
    ReminderCreateView,
    CgmCreateView,
    DashDetailView,
    DashHomeView,
)
from . import views

urlpatterns = [
    path('', DashHomeView.as_view(), name='dash-home'),
    path('detail/',DashDetailView.as_view(), name='dash-detail'),
    path('insulin/new/', InsulinCreateView.as_view(), name='insulin-create'),
    path('glucose/new/', GlucoseCreateView.as_view(), name='glucose-create'),
    path('insulin_changed/new/', InsulinChangedCreateView.as_view(), name='insulin_changed-create'),
    path('meal/new/', MealCreateView.as_view(), name='meal-create'),
    path('reminder/new/', ReminderCreateView.as_view(), name='reminder-create'),
    path('cgm/new/', CgmCreateView.as_view(), name='cgm-create'),
    path('log_event/',views.log_event, name='dash-log_event'),
    
    
   
]

