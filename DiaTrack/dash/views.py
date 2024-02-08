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

class DashListView(LoginRequiredMixin, ListView):
    
    template_name = 'dash/home.html'
    context_object_name = 'data_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insulin'] = Insulin.objects.filter(user=self.request.user)
        context['glucose'] = Glucose.objects.filter(user=self.request.user)
        context['insulin_changed'] = InsulinChanged.objects.filter(user=self.request.user)
        context['meal'] = Meal.objects.filter(user=self.request.user)
        context['reminder'] = Reminder.objects.filter(user=self.request.user)
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


   
