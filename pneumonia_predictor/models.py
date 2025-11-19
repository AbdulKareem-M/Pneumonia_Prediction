from django.db import models
from django.conf import settings

# Create your models here.

class Prediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    image_name = models.CharField(max_length=255)
    label = models.CharField(max_length=32)
    probability = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def image_url(self):
        return f"{settings.MEDIA_URL}{self.image_name}"
