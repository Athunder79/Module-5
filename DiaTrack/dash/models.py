from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class Insulin(models.Model):
    id = models.AutoField(primary_key=True)
    dose = models.DecimalField(max_digits=2, decimal_places=1)
    type = models.TextField()
    note = models.TextField()
    date_administered = models.DateTimeField(default=timezone.now)
    time_administered = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
	    return self.type

