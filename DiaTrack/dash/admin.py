from django.contrib import admin
from .models import Insulin, Glucose, InsulinChanged, Meal, Reminder, Cgm

admin.site.register(Insulin),
admin.site.register(Glucose),
admin.site.register(InsulinChanged),
admin.site.register(Meal),
admin.site.register(Reminder),
admin.site.register(Cgm)

# Register your models here.
