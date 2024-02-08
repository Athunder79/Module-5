from django.contrib import admin
from .models import Insulin, Glucose, InsulinChanged, Meal, Reminder

admin.site.register(Insulin),
admin.site.register(Glucose),
admin.site.register(InsulinChanged),
admin.site.register(Meal),
admin.site.register(Reminder)

# Register your models here.
