# detector_app/utils.py

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime


def send_prediction_email(patient_name, patient_email, label, probability):
    """
    Sends pneumonia prediction results (Normal or Pneumonia)
    using the corresponding HTML template.
    """

    # Select correct template
    if label == "Normal":
        template = "emails/prediction_normal.html"
    else:
        template = "emails/prediction_positive.html"

    # Render HTML
    html_content = render_to_string(template, {
        "patient_name": patient_name,
        "probability": probability,
        "year": datetime.now().year,
    })

    # Plain text fallback
    text_content = f"Your pneumonia test result: {label}"

    # Build email
    subject = "Your Pneumonia Screening Result - CityCare Hospital"

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[patient_email],
    )

    email.attach_alternative(html_content, "text/html")

    # Send
    email.send()
    return True
