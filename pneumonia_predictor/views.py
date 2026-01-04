# detector_app/views.py
import numpy as np
from django.shortcuts import render, redirect, get_object_or_404
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
import io
import os
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.contrib.auth.models import User
from .models import PendingUser
import random
from django.contrib.auth.hashers import make_password
from django.contrib import messages



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

            patient_name = request.POST.get("patient_name") or request.user.get_full_name() or request.user.username
            patient_email = request.POST.get("email") or request.user.email or ''

            Prediction.objects.create(
                user=request.user,
                image_name=img.name,
                patient_name=patient_name,
                patient_email=patient_email,
                label=result['label'],
                probability=result['probability']
            )

            send_prediction_email(
                patient_name=patient_name,
                patient_email=patient_email,
                label=result['label'],
                probability=result['probability']
            )

            return render(request, 'result.html', {
                'result': result,
                'image_url': image_url,
                'patient_name': patient_name,
                'patient_email': patient_email
            })
    else:
        form = UploadImageForm()

    return render(request, 'upload.html', {'form': form})


# new view: download user's predictions as PDF
@login_required(login_url='login')
def download_report(request):
    preds = Prediction.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'user': request.user,
        'predictions': preds,
    }
    html = render_to_string('reports/predictions_report.html', context)

    result = io.BytesIO()
    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=result, encoding='utf-8')
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="predictions_{request.user.username}.pdf"'
    return response

def _link_callback(uri, rel):
    """
    Convert HTML resource URIs to absolute system paths so xhtml2pdf can access them.
    Supports MEDIA_URL and STATIC_URL.
    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif hasattr(settings, 'STATIC_URL') and uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    else:
        # fallback: return as-is (may be remote)
        return uri

    if os.path.exists(path):
        return path
    return uri

@login_required(login_url='login')
def download_prediction_pdf(request, pk):
    # fetch prediction and enforce owner (allow staff)
    pred = get_object_or_404(Prediction, pk=pk)
    if pred.user != request.user and not request.user.is_staff:
        return HttpResponse('Forbidden', status=403)

    context = {'prediction': pred, 'user': request.user}
    html = render_to_string('reports/prediction_report.html', context)

    result = io.BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=result, encoding='utf-8', link_callback=_link_callback)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    filename = f"prediction_{pred.pk}.pdf"
    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

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
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate passwords
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Unique email check
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        if PendingUser.objects.filter(email=email).exists():
            messages.error(request, "You have a pending registration. Complete it.")
            return redirect('signup')

        # Generate OTP
        otp = str(random.randint(100000, 999999))

        pending = PendingUser.objects.create(
            email=email,
            username=username,
            password=make_password(password1),
            otp=otp
        )

        # SEND OTP EMAIL -- FIXED
        send_otp_email(username, email, otp)

        # REDIRECT PROPERLY
        return redirect("complete_registration", pending_id=pending.id)

    return render(request, "registration/signup.html")


from django.contrib.auth import login as auth_login

def complete_registration(request, pending_id):
    pending = get_object_or_404(PendingUser, id=pending_id)

    if request.method == "POST":
        uid = request.POST.get("uid")
        phone = request.POST.get("phone")
        otp = request.POST.get("otp")

        # validations
        if len(uid) != 16:
            messages.error(request, "UID must be 16 digits.")
            return redirect(request.path)

        if len(phone) != 10:
            messages.error(request, "Phone must be 10 digits.")
            return redirect(request.path)

        if otp != pending.otp:
            messages.error(request, "Invalid OTP.")
            return redirect(request.path)

        # Unique in PendingUser
        if PendingUser.objects.filter(uid_number=uid).exclude(id=pending_id).exists():
            messages.error(request, "UID already exists.")
            return redirect(request.path)

        if PendingUser.objects.filter(phone_number=phone).exclude(id=pending_id).exists():
            messages.error(request, "Phone number already exists.")
            return redirect(request.path)

        # Create actual user
        user = User.objects.create(
            username=pending.username,
            email=pending.email,
            password=pending.password,
        )

        pending.delete()
        auth_login(request, user)

        return redirect("registration_success")

    return render(request, "registration/complete_registration.html")



print()