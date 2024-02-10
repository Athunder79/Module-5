from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from django.http import HttpResponse
from .models import Insulin, Glucose, InsulinChanged, Meal, Reminder, Cgm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



def home(request):
    context = {
    }   
    return render(request, 'dash/home.html')

@login_required(login_url='login')
def detail(request):
    return render(request, 'dash/detail.html')

@login_required(login_url='login')
def log_event(request):
    return render(request, 'dash/log_event.html')


class DashListView(LoginRequiredMixin,ListView):   
    context_object_name = 'data_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insulin'] = Insulin.objects.filter(user=self.request.user)
        context['glucose'] = Glucose.objects.filter(user=self.request.user)
        context['insulin_changed'] = InsulinChanged.objects.filter(user=self.request.user)
        context['meal'] = Meal.objects.filter(user=self.request.user)
        context['reminder'] = Reminder.objects.filter(user=self.request.user)
        context['cgm'] = Cgm.objects.filter(user=self.request.user)

        for cgm in context['cgm']:
            time_passed = timezone.now() - cgm.date_changed
            print (time_passed)
            total_seconds = time_passed.total_seconds()
            print(total_seconds)
            days_left = cgm.sensor_life_in_days - (total_seconds // 86400)
            print(days_left)
            hours_left = (total_seconds % 86400) // 3600
            print(hours_left)
            cgm.remaining_days = int(days_left)
            cgm.remaining_time = int(hours_left)

            
        for insulin_changed in context['insulin_changed']:
            time_passed = timezone.now() - insulin_changed.date_changed
            total_seconds = time_passed.total_seconds()
            days_left = 28 - (total_seconds // 86400)
            hours_left = (total_seconds % 86400) // 3600
            insulin_changed.remaining_days = int(days_left)
            insulin_changed.remaining_time = int(hours_left)
            
        return context        
       
        
    def get_queryset(self):
        # Override the get_queryset method 
        return Insulin.objects.none()
    
    
    
class DashDetailView(DashListView):
    template_name = 'dash/detail.html'

    def get_queryset(self):
        # Override the get_queryset method 
        return Insulin.objects.none()
    
class DashHomeView(DashListView):
    template_name = 'dash/home.html'

    def get_queryset(self):
        # Override the get_queryset method 
        return Insulin.objects.none()
    

class InsulinCreateView(CreateView):
    model = Insulin
    fields = ['dose', 'insulin_type', 'note', 'date_administered',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GlucoseCreateView(CreateView):
    model = Glucose
    fields = ['reading', 'note', 'date_taken',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class InsulinChangedCreateView(CreateView):
    model = InsulinChanged
    fields = ['insulin_type', 'date_changed']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MealCreateView(CreateView):  
    model = Meal    
    fields = ['meal', 'total_carb_intake', 'note', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReminderCreateView(CreateView):
    model = Reminder
    fields = ['reminder', 'date', 'date_due']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CgmCreateView(CreateView):
    model = Cgm
    fields = ['sensor', 'sensor_life_in_days','date_changed']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

   


   
