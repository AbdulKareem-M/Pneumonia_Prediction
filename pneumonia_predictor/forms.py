# detector_app/forms.py
from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField(label="Upload Chest X-ray")
    patient_name = forms.CharField(max_length=100)
    email = forms.EmailField()

