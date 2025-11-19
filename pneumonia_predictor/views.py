# detector_app/views.py
import os
import numpy as np
from django.shortcuts import render, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from .forms import UploadImageForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Prediction
from django.db.models import Count
from .utils.email_utils import *

# Load model once at startup
MODEL_PATH = os.path.join(settings.BASE_DIR, 'pneumonia_predictor', 'models', 'pneumonia_model.h5')
model = load_model(MODEL_PATH)
print("✅ Model loaded successfully!")

def predict_pneumonia(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    prob = float(prediction[0][0])
    print(f"Prediction confidence: {prob:.4f}")
    
    label = "Normal" if prob > 0.5 else "Pneumonia"
    # return both label and probability for UI
    return {"label": label, "probability": prob}


@login_required(login_url='login')
def upload_and_predict(request):
    result = None
    image_url = None
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            img_path = os.path.join(settings.MEDIA_ROOT, img.name)
            with open(img_path, 'wb+') as f:
                for chunk in img.chunks():
                    f.write(chunk)
            result = predict_pneumonia(img_path)
            image_url = settings.MEDIA_URL + img.name

            # persist prediction for dashboard
            try:
                Prediction.objects.create(
                    user=request.user,
                    image_name=img.name,
                    label=result['label'],
                    probability=result['probability']
                )
            except Exception as e:
                # don't break the request on DB errors; log if needed
                print("Prediction save failed:", e)
            
            
            # ---------------------------------------
            # SEND HTML EMAIL USING UTILITY FUNCTION
            # ---------------------------------------
            try:
                patient_name = request.POST.get("patient_name", request.user.username)
                patient_email = request.POST.get("email", request.user.email)

                send_prediction_email(
                    patient_name=patient_name,
                    patient_email=patient_email,
                    label=result['label'],
                    probability=result['probability']
                )
                print("Email sent successfully!")
            except Exception as e:
                print("Email sending failed:", e)
            # ---------------------------------------

    else:
        form = UploadImageForm()

    return render(request, 'upload.html', {'form': form, 'result': result, 'image_url': image_url})

@login_required(login_url='login')
def dashboard(request):
    total = Prediction.objects.filter(user=request.user).count()
    pneumonia = Prediction.objects.filter(label='Pneumonia', user =request.user).count()
    normal = Prediction.objects.filter(label='Normal', user = request.user).count()
    # show recent predictions for current user
    recent = Prediction.objects.filter(user=request.user)[:20]
    return render(request, 'dashboard.html', {
        'total': total,
        'pneumonia': pneumonia,
        'normal': normal,
        'recent': recent,
    })

def signup(request):
    """
    Simple user registration using Django's UserCreationForm.
    Logs the user in on successful registration and redirects to the app.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('upload_and_predict')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

print()