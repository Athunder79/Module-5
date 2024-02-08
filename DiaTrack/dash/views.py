from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Insulin, Glucose, InsulinChanged, Meal, Reminder
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



def home(request):
    context = {
    }   
    return render(request, 'dash/home.html')

def detail(request):
    return HttpResponse('<h1>detail</h1>')

class DashListView(ListView):
    
    template_name = 'dash/home.html'
    context_object_name = 'data_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insulin'] = Insulin.objects.all()
        context['glucose'] = Glucose.objects.all()
        context['insulin_changed'] = InsulinChanged.objects.all()
        context['meal'] = Meal.objects.all()
        context['reminder'] = Reminder.objects.all()
        return context
        
    def get_queryset(self):
        # Override the get_queryset method 
        return Insulin.objects.none()

class InsulinCreateView(CreateView):
    model = Insulin
    fields = ['dose', 'insulin_type', 'note', 'date_administered', 'time_administered']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GlucoseCreateView(CreateView):
    model = Glucose
    fields = ['reading', 'note', 'date_taken', 'time_taken']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class InsulinChangedCreateView(CreateView):
    model = InsulinChanged
    fields = ['insulin_type', 'date_changed', 'time_changed']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MealCreateView(CreateView):  
    model = Meal    
    fields = ['meal', 'total_carb_intake', 'note', 'date', 'time']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReminderCreateView(CreateView):
    model = Reminder
    fields = ['reminder', 'date', 'date_due']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

   


   
