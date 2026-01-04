
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import uuid


class Prediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=255)
    # new fields to store patient details
    patient_name = models.CharField(max_length=255, blank=True, null=True)
    patient_email = models.EmailField(blank=True, null=True)
    label = models.CharField(max_length=32)
    probability = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def image_url(self):
        return f"{settings.MEDIA_URL}{self.image_name}"
    

class PendingUser(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    password = models.CharField(max_length=200)  # hashed password
    otp = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)

    uid_number = models.CharField(max_length=12, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True, unique=True)

    def __str__(self):
        return self.email
