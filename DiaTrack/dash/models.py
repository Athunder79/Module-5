from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

class Insulin(models.Model):
    id = models.AutoField(primary_key=True)
    dose = models.DecimalField(max_digits=2, decimal_places=1)
    insulin_type = models.TextField()
    note = models.TextField(null=True, blank=True)
    date_administered = models.DateTimeField(default=timezone.now)
    time_administered = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
	    return self.type

    def get_absolute_url(self): 
        return reverse('dash-home')

class Glucose(models.Model):
    id = models.AutoField(primary_key=True)
    reading = models.DecimalField(max_digits=3, decimal_places=1)
    note = models.TextField(null=True, blank=True)
    date_taken = models.DateTimeField(default=timezone.now)
    time_taken = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note

    def get_absolute_url(self): 
        return reverse('dash-home')    


class InsulinChanged(models.Model):
    id = models.AutoField(primary_key=True)
    insulin_type = models.TextField()
    date_changed = models.DateTimeField(default=timezone.now)
    time_changed = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.insulin_type

    def get_absolute_url(self): 
        return reverse('dash-home')


class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    meal = models.TextField()
    total_card_intake = models.DecimalField(max_digits=3, decimal_places=1)
    note = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal

    def get_absolute_url(self): 
        return reverse('dash-home')

  

class Reminder(models.Model):
    id = models.AutoField(primary_key=True)
    reminder = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    date_due = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.reminder

    def get_absolute_url(self): 
        return reverse('dash-home')
