from django.contrib import admin
from .models import PendingUser, Prediction

admin.site.register(PendingUser)
admin.site.register(Prediction)
