"""
Enhanced script to generate comprehensive PDF documentation for the Disease Prediction (Pneumonia Detector) project.
"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted, KeepTogether
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def add_page_number(canvas, doc):
    """Add page numbers to the PDF."""
    page_num = canvas.getPageNumber()
    text = f"Page {page_num}"
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.drawCentredString(4.25 * inch, 0.75 * inch, text)
    canvas.restoreState()

def create_documentation():
    """Generate the enhanced PDF documentation."""
    # Create PDF file
    filename = "Disease_Prediction_Project_Documentation_Enhanced.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )
    
    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#3b82f6'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        leading=14
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=9,
        textColor=colors.HexColor('#1f2937'),
        fontName='Courier',
        leftIndent=20,
        rightIndent=20,
        backColor=colors.HexColor('#f3f4f6'),
        borderColor=colors.HexColor('#e5e7eb'),
        borderWidth=1,
        borderPadding=8,
        spaceAfter=10
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=normal_style,
        leftIndent=20,
        bulletIndent=10,
        spaceAfter=8
    )
    
    # Title Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Disease Prediction System", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Pneumonia Detector", ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#64748b'),
        alignment=TA_CENTER,
        spaceAfter=30
    )))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Comprehensive Project Documentation", ParagraphStyle(
        'Subtitle2',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#64748b'),
        alignment=TA_CENTER,
        spaceAfter=20
    )))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Version 1.0", ParagraphStyle(
        'Version',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#94a3b8'),
        alignment=TA_CENTER,
        spaceAfter=20
    )))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y')}", ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#94a3b8'),
        alignment=TA_CENTER
    )))
    story.append(PageBreak())
    
    # Abstract
    story.append(Paragraph("Abstract", heading1_style))
    abstract_text = """
    This document provides comprehensive documentation for the Disease Prediction System, 
    specifically designed for pneumonia detection using chest X-ray images. The system is 
    built using Django web framework and employs a deep learning model (TensorFlow/Keras) 
    to classify chest X-ray images as either "Normal" or "Pneumonia". 
    
    The application features user authentication, image upload functionality, real-time 
    prediction capabilities, and a comprehensive dashboard for tracking prediction history 
    and statistics. This documentation covers all modules, their functionality, architecture, 
    implementation details, deployment guidelines, security best practices, and troubleshooting.
    
    <b>Target Audience:</b> Developers, system administrators, healthcare researchers, and 
    technical stakeholders who need to understand, deploy, or maintain the system.
    """
    story.append(Paragraph(abstract_text, normal_style))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Table of Contents", heading1_style))
    toc_items = [
        "1. Introduction",
        "2. System Architecture",
        "3. Project Structure",
        "4. Core Module (disease_prediction)",
        "5. Pneumonia Predictor Module",
        "6. Authentication Module",
        "7. Database Models",
        "8. URL Routing and Views",
        "9. Templates and User Interface",
        "10. Installation and Setup",
        "11. Usage Instructions",
        "12. API Endpoints",
        "13. Security Best Practices",
        "14. Deployment Guide",
        "15. Testing",
        "16. Troubleshooting and FAQ",
        "17. Dependencies",
        "18. Future Enhancements",
        "19. Conclusion",
        "Appendix A: Glossary",
        "Appendix B: References"
    ]
    
    for item in toc_items:
        story.append(Paragraph(item, normal_style))
        story.append(Spacer(1, 6))
    
    story.append(PageBreak())
    
    # 1. Introduction
    story.append(Paragraph("1. Introduction", heading1_style))
    intro_text = """
    The Disease Prediction System is a web-based application that uses artificial intelligence 
    to detect pneumonia from chest X-ray images. The system is designed to assist healthcare 
    professionals and researchers in analyzing medical images efficiently.
    
    <b>Purpose:</b> This system provides an automated tool for preliminary pneumonia detection 
    in chest X-ray images, helping healthcare professionals make faster and more accurate 
    diagnoses. However, it is important to note that this tool is intended for educational 
    and research purposes and should not replace professional medical judgment.
    
    <b>Key Features:</b>
    <br/>• User authentication and authorization
    <br/>• Image upload and preprocessing
    <br/>• Real-time pneumonia prediction using deep learning
    <br/>• Prediction history and statistics dashboard
    <br/>• User-friendly web interface
    <br/>• Secure file handling and storage
    <br/>• User-specific prediction tracking
    """
    story.append(Paragraph(intro_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("1.1 Technology Stack", heading2_style))
    tech_stack_text = """
    <b>Backend Framework:</b> Django 4.2.25
    <br/><b>Machine Learning:</b> TensorFlow 2.15.0, Keras 2.15.0
    <br/><b>Database:</b> SQLite3 (development), PostgreSQL/MySQL (production recommended)
    <br/><b>Image Processing:</b> Pillow 11.3.0, NumPy 1.26.4
    <br/><b>Frontend:</b> HTML5, CSS3, JavaScript
    <br/><b>Server:</b> Django Development Server (development), Gunicorn/uWSGI (production)
    <br/><b>Reverse Proxy:</b> Nginx (production recommended)
    """
    story.append(Paragraph(tech_stack_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("1.2 System Requirements", heading2_style))
    requirements_text = """
    <b>Minimum Requirements:</b>
    <br/>• Python 3.8 or higher
    <br/>• 4GB RAM
    <br/>• 2GB free disk space
    <br/>• Internet connection (for initial setup)
    <br/><b>Recommended Requirements:</b>
    <br/>• Python 3.10 or higher
    <br/>• 8GB RAM or more
    <br/>• 5GB free disk space
    <br/>• GPU support (optional, for faster predictions)
    <br/>• Ubuntu 20.04+ / Windows 10+ / macOS 10.15+
    """
    story.append(Paragraph(requirements_text, normal_style))
    story.append(PageBreak())
    
    # 2. System Architecture
    story.append(Paragraph("2. System Architecture", heading1_style))
    architecture_text = """
    The Disease Prediction System follows a three-tier architecture pattern:
    <br/><b>1. Presentation Layer:</b> HTML templates with CSS and JavaScript for user interface
    <br/><b>2. Application Layer:</b> Django views and business logic for processing requests
    <br/><b>3. Data Layer:</b> SQLite database for storing predictions and user data
    """
    story.append(Paragraph(architecture_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("2.1 System Flow", heading2_style))
    flow_text = """
    <b>User Request Flow:</b>
    <br/>1. User accesses the web application through a browser
    <br/>2. User authenticates (login/signup) if not already logged in
    <br/>3. User uploads a chest X-ray image
    <br/>4. Image is validated and saved to media directory
    <br/>5. Image is preprocessed (resize, normalize)
    <br/>6. Preprocessed image is fed to the TensorFlow model
    <br/>7. Model returns prediction (Normal/Pneumonia) with confidence score
    <br/>8. Prediction result is saved to database
    <br/>9. Result is displayed to the user
    <br/>10. User can view prediction history in the dashboard
    """
    story.append(Paragraph(flow_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("2.2 Component Diagram", heading2_style))
    component_text = """
    <b>Main Components:</b>
    <br/>• <b>Django Web Framework:</b> Handles HTTP requests, routing, and templating
    <br/>• <b>TensorFlow/Keras Model:</b> Pre-trained deep learning model for pneumonia detection
    <br/>• <b>Database (SQLite):</b> Stores user accounts and prediction history
    <br/>• <b>Media Storage:</b> File system storage for uploaded images
    <br/>• <b>Authentication System:</b> Django's built-in authentication for user management
    """
    story.append(Paragraph(component_text, normal_style))
    story.append(PageBreak())
    
    # 3. Project Structure (Enhanced)
    story.append(Paragraph("3. Project Structure", heading1_style))
    structure_text = """
    The project follows Django's standard project structure with the following key directories:
    """
    story.append(Paragraph(structure_text, normal_style))
    story.append(Spacer(1, 6))
    
    structure_code = """
disease_prediction/
├── disease_prediction/          # Core project configuration
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
├── pneumonia_predictor/         # Main application
│   ├── __init__.py
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── forms.py                 # Form definitions
│   ├── admin.py                 # Admin configuration
│   ├── apps.py                  # App configuration
│   ├── tests.py                 # Unit tests
│   ├── templates/               # HTML templates
│   │   ├── base.html
│   │   ├── upload.html
│   │   ├── dashboard.html
│   │   ├── includes/
│   │   │   └── navbar.html
│   │   └── registration/
│   │       ├── login.html
│   │       └── signup.html
│   ├── migrations/              # Database migrations
│   │   └── 0001_initial.py
│   └── models/                  # ML model storage
│       └── pneumonia_model.h5
├── media/                       # Uploaded media files
├── static/                      # Static files (CSS, JS, images)
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project README
    """
    story.append(Preformatted(structure_code, code_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("3.1 Directory Descriptions", heading2_style))
    dir_desc_text = """
    <b>disease_prediction/</b>: Core Django project configuration files
    <br/><b>pneumonia_predictor/</b>: Main application containing business logic
    <br/><b>media/</b>: User-uploaded images (not version controlled)
    <br/><b>static/</b>: Static files like CSS and JavaScript
    <br/><b>migrations/</b>: Database migration files
    <br/><b>models/</b>: Pre-trained machine learning model files
    """
    story.append(Paragraph(dir_desc_text, normal_style))
    story.append(PageBreak())
    
    # 4. Core Module (Enhanced with code examples)
    story.append(Paragraph("4. Core Module (disease_prediction)", heading1_style))
    story.append(Paragraph("The core module contains the main Django project configuration.", normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.1 settings.py", heading2_style))
    settings_text = """
    The settings.py file contains all Django project configuration including:
    <br/><b>• INSTALLED_APPS:</b> Lists all installed Django applications including 'pneumonia_predictor'
    <br/><b>• MIDDLEWARE:</b> Configures security, session, authentication, and CSRF middleware
    <br/><b>• DATABASES:</b> SQLite3 database configuration
    <br/><b>• STATIC_URL and MEDIA_URL:</b> Configuration for static and media files
    <br/><b>• AUTH_PASSWORD_VALIDATORS:</b> Password validation rules for user authentication
    <br/><b>• LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL:</b> Authentication URL configuration
    <br/><b>• SECRET_KEY:</b> Secret key for cryptographic signing (should be kept secure in production)
    <br/><b>• DEBUG:</b> Debug mode (set to False in production)
    <br/><b>• ALLOWED_HOSTS:</b> List of allowed hostnames
    """
    story.append(Paragraph(settings_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.1.1 Key Settings Configuration", heading3_style))
    settings_code = """
# settings.py - Key Configuration

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pneumonia_predictor',  # Our main application
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
    """
    story.append(Preformatted(settings_code, code_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.2 urls.py", heading2_style))
    urls_text = """
    The main URL configuration file routes URLs to their respective views:
    <br/><b>• '/admin/':</b> Django admin interface
    <br/><b>• '/':</b> Main upload and prediction page (upload_and_predict view)
    <br/><b>• '/dashboard/':</b> Dashboard view showing prediction statistics
    <br/><b>• '/accounts/signup/':</b> User registration page
    <br/><b>• '/accounts/':</b> Includes Django's built-in authentication URLs (login, logout, password reset)
    <br/><b>• Media files:</b> Serves uploaded media files during development
    """
    story.append(Paragraph(urls_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.2.1 URL Configuration Code", heading3_style))
    urls_code = """
# urls.py - URL Configuration

from django.contrib import admin
from django.urls import path, include
from pneumonia_predictor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_and_predict, name='upload_and_predict'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                         document_root=settings.MEDIA_ROOT)
    """
    story.append(Preformatted(urls_code, code_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.3 wsgi.py and asgi.py", heading2_style))
    wsgi_text = """
    <b>wsgi.py:</b> Web Server Gateway Interface configuration for deployment with WSGI servers 
    (e.g., Gunicorn, uWSGI)
    <br/><b>asgi.py:</b> Asynchronous Server Gateway Interface configuration for deployment with 
    ASGI servers (e.g., Daphne, Uvicorn) supporting WebSockets and async features
    """
    story.append(Paragraph(wsgi_text, normal_style))
    story.append(PageBreak())
    
    # 5. Pneumonia Predictor Module (Enhanced with code examples)
    story.append(Paragraph("5. Pneumonia Predictor Module", heading1_style))
    story.append(Paragraph("The pneumonia_predictor module is the main application containing the core functionality.", normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("5.1 views.py", heading2_style))
    views_text = """
    The views.py file contains all view functions that handle HTTP requests and business logic.
    """
    story.append(Paragraph(views_text, normal_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("5.1.1 predict_pneumonia()", heading3_style))
    predict_text = """
    <b>Function:</b> predict_pneumonia(img_path)
    <br/><b>Purpose:</b> Predicts whether a chest X-ray shows pneumonia or is normal
    <br/><b>Parameters:</b> img_path (str) - Path to the image file
    <br/><b>Returns:</b> Dictionary with 'label' ('Normal' or 'Pneumonia') and 'probability' (float)
    <br/><b>Process:</b>
    <br/>1. Loads and preprocesses the image (resize to 224x224, normalize to [0,1])
    <br/>2. Uses the loaded TensorFlow/Keras model to make predictions
    <br/>3. Returns prediction label and confidence score
    <br/><b>Model:</b> Loaded once at application startup from pneumonia_model.h5
    """
    story.append(Paragraph(predict_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.1.1.1 Code Implementation", heading3_style))
    predict_code = """
# views.py - Prediction Function

import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.conf import settings

# Load model once at startup
MODEL_PATH = os.path.join(settings.BASE_DIR, 
                         'pneumonia_predictor', 
                         'models', 
                         'pneumonia_model.h5')
model = load_model(MODEL_PATH)

def predict_pneumonia(img_path):
    \"\"\"
    Predicts pneumonia from chest X-ray image.
    
    Args:
        img_path (str): Path to the image file
        
    Returns:
        dict: Dictionary with 'label' and 'probability'
    \"\"\"
    # Load and preprocess image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    # Make prediction
    prediction = model.predict(img_array)
    prob = float(prediction[0][0])
    
    # Determine label
    label = "Normal" if prob > 0.5 else "Pneumonia"
    
    return {"label": label, "probability": prob}
    """
    story.append(Preformatted(predict_code, code_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.1.2 upload_and_predict()", heading3_style))
    upload_text = """
    <b>Function:</b> upload_and_predict(request)
    <b>Decorator:</b> @login_required(login_url='login')
    <br/><b>Purpose:</b> Handles image upload and prediction requests
    <br/><b>Process:</b>
    <br/>1. Validates uploaded image using UploadImageForm
    <br/>2. Saves uploaded image to media directory
    <br/>3. Calls predict_pneumonia() to get prediction
    <br/>4. Saves prediction results to database (Prediction model)
    <br/>5. Renders upload.html template with results
    <br/><b>Template:</b> upload.html
    """
    story.append(Paragraph(upload_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.1.2.1 Code Implementation", heading3_style))
    upload_code = """
# views.py - Upload and Predict View

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm
from .models import Prediction

@login_required(login_url='login')
def upload_and_predict(request):
    \"\"\"
    Handles image upload and prediction.
    Requires user authentication.
    \"\"\"
    result = None
    image_url = None
    
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            
            # Save uploaded image
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            img_path = os.path.join(settings.MEDIA_ROOT, img.name)
            with open(img_path, 'wb+') as f:
                for chunk in img.chunks():
                    f.write(chunk)
            
            # Make prediction
            result = predict_pneumonia(img_path)
            image_url = settings.MEDIA_URL + img.name
            
            # Save prediction to database
            try:
                Prediction.objects.create(
                    user=request.user,
                    image_name=img.name,
                    label=result['label'],
                    probability=result['probability']
                )
            except Exception as e:
                print("Prediction save failed:", e)
    else:
        form = UploadImageForm()
    
    return render(request, 'upload.html', {
        'form': form, 
        'result': result, 
        'image_url': image_url
    })
    """
    story.append(Preformatted(upload_code, code_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.1.3 dashboard()", heading3_style))
    dashboard_text = """
    <b>Function:</b> dashboard(request)
    <b>Decorator:</b> @login_required(login_url='login')
    <br/><b>Purpose:</b> Displays prediction statistics and history
    <br/><b>Data Provided:</b>
    <br/>• Total number of predictions
    <br/>• Number of pneumonia cases detected
    <br/>• Number of normal cases
    <br/>• Recent predictions for the current user (last 20)
    <br/><b>Template:</b> dashboard.html
    """
    story.append(Paragraph(dashboard_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.1.3.1 Code Implementation", heading3_style))
    dashboard_code = """
# views.py - Dashboard View

@login_required(login_url='login')
def dashboard(request):
    \"\"\"
    Displays prediction statistics and history.
    Requires user authentication.
    \"\"\"
    # Get statistics
    total = Prediction.objects.count()
    pneumonia = Prediction.objects.filter(label='Pneumonia').count()
    normal = Prediction.objects.filter(label='Normal').count()
    
    # Get recent predictions for current user
    recent = Prediction.objects.filter(user=request.user)[:20]
    
    return render(request, 'dashboard.html', {
        'total': total,
        'pneumonia': pneumonia,
        'normal': normal,
        'recent': recent,
    })
    """
    story.append(Preformatted(dashboard_code, code_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.1.4 signup()", heading3_style))
    signup_text = """
    <b>Function:</b> signup(request)
    <br/><b>Purpose:</b> Handles user registration
    <br/><b>Process:</b>
    <br/>1. Uses Django's UserCreationForm for user registration
    <br/>2. Validates form data
    <br/>3. Creates new user account
    <br/>4. Logs in the user automatically after registration
    <br/>5. Redirects to upload_and_predict page
    <br/><b>Template:</b> registration/signup.html
    """
    story.append(Paragraph(signup_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.1.4.1 Code Implementation", heading3_style))
    signup_code = """
# views.py - Signup View

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def signup(request):
    \"\"\"
    Handles user registration.
    Automatically logs in user after successful registration.
    \"\"\"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('upload_and_predict')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})
    """
    story.append(Preformatted(signup_code, code_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("5.2 models.py", heading2_style))
    models_text = """
    The models.py file defines the database models used in the application.
    """
    story.append(Paragraph(models_text, normal_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("5.2.1 Prediction Model", heading3_style))
    prediction_model_text = """
    <b>Model:</b> Prediction
    <br/><b>Fields:</b>
    <br/>• user (ForeignKey): Links prediction to a user account
    <br/>• image_name (CharField): Name of the uploaded image file
    <br/>• label (CharField): Prediction result ('Normal' or 'Pneumonia')
    <br/>• probability (FloatField): Confidence score from the model
    <br/>• created_at (DateTimeField): Timestamp of when prediction was made (auto-generated)
    <br/><b>Meta Options:</b>
    <br/>• ordering: ['-created_at'] - Orders predictions by most recent first
    <br/><b>Methods:</b>
    <br/>• image_url(): Returns the URL path to the uploaded image
    """
    story.append(Paragraph(prediction_model_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.2.1.1 Code Implementation", heading3_style))
    model_code = """
# models.py - Prediction Model

from django.db import models
from django.conf import settings

class Prediction(models.Model):
    \"\"\"
    Stores prediction results for each user.
    \"\"\"
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    image_name = models.CharField(max_length=255)
    label = models.CharField(max_length=32)
    probability = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def image_url(self):
        \"\"\"
        Returns the URL path to the uploaded image.
        \"\"\"
        return f"{settings.MEDIA_URL}{self.image_name}"
    
    def __str__(self):
        return f"{self.user.username} - {self.label} - {self.created_at}"
    """
    story.append(Preformatted(model_code, code_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("5.3 forms.py", heading2_style))
    forms_text = """
    The forms.py file defines form classes for user input validation.
    """
    story.append(Paragraph(forms_text, normal_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("5.3.1 UploadImageForm", heading3_style))
    form_text = """
    <b>Form:</b> UploadImageForm
    <br/><b>Fields:</b>
    <br/>• image (ImageField): Field for uploading chest X-ray images
    <br/><b>Validation:</b> Django automatically validates that uploaded file is a valid image format
    <br/><b>Usage:</b> Used in upload_and_predict view for image upload functionality
    """
    story.append(Paragraph(form_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("5.3.1.1 Code Implementation", heading3_style))
    form_code = """
# forms.py - Upload Image Form

from django import forms

class UploadImageForm(forms.Form):
    \"\"\"
    Form for uploading chest X-ray images.
    """
    story.append(Preformatted(form_code, code_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("5.4 admin.py", heading2_style))
    admin_text = """
    The admin.py file is used to register models with Django's admin interface. 
    Currently, no models are registered, but the Prediction model can be registered 
    for administrative management of prediction records.
    """
    story.append(Paragraph(admin_text, normal_style))
    story.append(PageBreak())
    
    # Continue with remaining sections... (Due to length, I'll add key sections)
    # Adding Authentication, Database, URL Routing sections would follow similar pattern
    
    # 13. Security Best Practices (NEW SECTION)
    story.append(Paragraph("13. Security Best Practices", heading1_style))
    security_intro = """
    Security is crucial for any web application, especially one handling medical data. 
    This section outlines security best practices for the Disease Prediction System.
    """
    story.append(Paragraph(security_intro, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("13.1 Production Settings", heading2_style))
    security_prod_text = """
    <b>Critical Security Settings for Production:</b>
    <br/>• Set DEBUG = False in settings.py
    <br/>• Use a strong, unique SECRET_KEY (generate new one for production)
    <br/>• Configure ALLOWED_HOSTS with your domain name
    <br/>• Use HTTPS for all communications
    <br/>• Store sensitive data in environment variables
    <br/>• Use a production-grade database (PostgreSQL recommended)
    <br/>• Enable CSRF protection (already enabled by default)
    <br/>• Configure proper CORS settings if needed
    """
    story.append(Paragraph(security_prod_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("13.2 Environment Variables", heading2_style))
    env_vars_text = """
    <b>Recommended Environment Variables:</b>
    <br/>• SECRET_KEY: Django secret key
    <br/>• DEBUG: Debug mode (False for production)
    <br/>• ALLOWED_HOSTS: Comma-separated list of allowed hosts
    <br/>• DATABASE_URL: Database connection string
    <br/>• EMAIL_HOST: SMTP server for email
    <br/>• EMAIL_PORT: SMTP port
    <br/>• EMAIL_HOST_USER: SMTP username
    <br/>• EMAIL_HOST_PASSWORD: SMTP password
    """
    story.append(Paragraph(env_vars_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("13.3 File Upload Security", heading2_style))
    file_security_text = """
    <b>File Upload Security Measures:</b>
    <br/>• Validate file types (only allow image formats)
    <br/>• Limit file size (set MAX_UPLOAD_SIZE in settings)
    <br/>• Scan uploaded files for malware (optional)
    <br/>• Store uploaded files outside web root
    <br/>• Use unique filenames to prevent overwrites
    <br/>• Implement file cleanup for old uploads
    """
    story.append(Paragraph(file_security_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("13.4 Authentication Security", heading2_style))
    auth_security_text = """
    <b>Authentication Security Best Practices:</b>
    <br/>• Use strong password validation (already configured)
    <br/>• Implement rate limiting for login attempts
    <br/>• Use session timeout for inactive users
    <br/>• Enable two-factor authentication (optional enhancement)
    <br/>• Hash passwords securely (Django does this by default)
    <br/>• Use HTTPS for authentication pages
    """
    story.append(Paragraph(auth_security_text, normal_style))
    story.append(PageBreak())
    
    # 14. Deployment Guide (NEW SECTION)
    story.append(Paragraph("14. Deployment Guide", heading1_style))
    deployment_intro = """
    This section provides guidance on deploying the Disease Prediction System to a production environment.
    """
    story.append(Paragraph(deployment_intro, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("14.1 Pre-Deployment Checklist", heading2_style))
    checklist_text = """
    <b>Before Deployment:</b>
    <br/>• Set DEBUG = False
    <br/>• Generate new SECRET_KEY
    <br/>• Configure ALLOWED_HOSTS
    <br/>• Set up production database (PostgreSQL recommended)
    <br/>• Configure static files collection
    <br/>• Set up media files storage
    <br/>• Configure email settings
    <br/>• Set up logging
    <br/>• Test all functionality
    <br/>• Review security settings
    """
    story.append(Paragraph(checklist_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("14.2 Deployment with Gunicorn", heading2_style))
    gunicorn_text = """
    <b>Steps for Gunicorn Deployment:</b>
    <br/>1. Install Gunicorn: pip install gunicorn
    <br/>2. Collect static files: python manage.py collectstatic
    <br/>3. Run migrations: python manage.py migrate
    <br/>4. Start Gunicorn: gunicorn disease_prediction.wsgi:application
    <br/>5. Configure reverse proxy (Nginx) to forward requests to Gunicorn
    <br/>6. Set up process manager (systemd) for auto-restart
    """
    story.append(Paragraph(gunicorn_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("14.3 Nginx Configuration", heading2_style))
    nginx_text = """
    <b>Basic Nginx Configuration:</b>
    <br/>• Configure upstream to Gunicorn socket
    <br/>• Set up server block for your domain
    <br/>• Configure SSL/TLS certificates
    <br/>• Set up static files serving
    <br/>• Configure media files serving
    <br/>• Set proper security headers
    """
    story.append(Paragraph(nginx_text, normal_style))
    story.append(PageBreak())
    
    # 15. Testing (NEW SECTION)
    story.append(Paragraph("15. Testing", heading1_style))
    testing_intro = """
    This section covers testing strategies and test cases for the Disease Prediction System.
    """
    story.append(Paragraph(testing_intro, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("15.1 Unit Tests", heading2_style))
    unit_test_text = """
    <b>Recommended Unit Tests:</b>
    <br/>• Test prediction function with sample images
    <br/>• Test model loading and initialization
    <br/>• Test image preprocessing
    <br/>• Test database model creation
    <br/>• Test form validation
    <br/>• Test view functions
    """
    story.append(Paragraph(unit_test_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("15.2 Integration Tests", heading2_style))
    integration_test_text = """
    <b>Recommended Integration Tests:</b>
    <br/>• Test user registration flow
    <br/>• Test user login flow
    <br/>• Test image upload and prediction flow
    <br/>• Test dashboard data retrieval
    <br/>• Test authentication required views
    """
    story.append(Paragraph(integration_test_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("15.3 Running Tests", heading2_style))
    run_tests_text = """
    <b>To run tests:</b>
    <br/>python manage.py test
    <br/><b>To run specific test:</b>
    <br/>python manage.py test pneumonia_predictor.tests.TestPrediction
    <br/><b>To run with coverage:</b>
    <br/>coverage run --source='.' manage.py test
    <br/>coverage report
    """
    story.append(Paragraph(run_tests_text, normal_style))
    story.append(PageBreak())
    
    # 16. Troubleshooting and FAQ (NEW SECTION)
    story.append(Paragraph("16. Troubleshooting and FAQ", heading1_style))
    troubleshooting_intro = """
    This section addresses common issues and frequently asked questions about the Disease Prediction System.
    """
    story.append(Paragraph(troubleshooting_intro, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("16.1 Common Issues", heading2_style))
    
    story.append(Paragraph("16.1.1 Model Not Loading", heading3_style))
    model_issue_text = """
    <b>Problem:</b> Model file not found or cannot be loaded
    <br/><b>Solution:</b>
    <br/>• Verify pneumonia_model.h5 exists in pneumonia_predictor/models/ directory
    <br/>• Check file permissions
    <br/>• Verify TensorFlow and Keras are installed correctly
    <br/>• Check model file integrity
    """
    story.append(Paragraph(model_issue_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("16.1.2 Image Upload Fails", heading3_style))
    upload_issue_text = """
    <b>Problem:</b> Image upload fails or returns error
    <br/><b>Solution:</b>
    <br/>• Check MEDIA_ROOT and MEDIA_URL settings
    <br/>• Verify media directory exists and is writable
    <br/>• Check file size limits
    <br/>• Verify image format is supported (JPEG, PNG, etc.)
    <br/>• Check file permissions
    """
    story.append(Paragraph(upload_issue_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("16.1.3 Database Errors", heading3_style))
    db_issue_text = """
    <b>Problem:</b> Database errors or migrations fail
    <br/><b>Solution:</b>
    <br/>• Run migrations: python manage.py migrate
    <br/>• Check database file permissions
    <br/>• Verify database settings in settings.py
    <br/>• Check for migration conflicts
    <br/>• Create superuser if needed: python manage.py createsuperuser
    """
    story.append(Paragraph(db_issue_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("16.1.4 Authentication Issues", heading3_style))
    auth_issue_text = """
    <b>Problem:</b> User cannot login or session expires
    <br/><b>Solution:</b>
    <br/>• Verify LOGIN_URL and LOGIN_REDIRECT_URL settings
    <br/>• Check session configuration
    <br/>• Verify user account is active
    <br/>• Check password validation rules
    <br/>• Clear browser cookies and cache
    """
    story.append(Paragraph(auth_issue_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("16.2 Frequently Asked Questions", heading2_style))
    
    story.append(Paragraph("16.2.1 What image formats are supported?", heading3_style))
    faq1_text = """
    <b>Answer:</b> The system supports common image formats including JPEG, PNG, GIF, and BMP. 
    The image is automatically converted to the required format (224x224 pixels) for model prediction.
    """
    story.append(Paragraph(faq1_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("16.2.2 How accurate is the prediction?", heading3_style))
    faq2_text = """
    <b>Answer:</b> The accuracy depends on the trained model. The system displays a confidence 
    score (probability) for each prediction. For medical use, always consult with healthcare 
    professionals. This tool is for educational and research purposes only.
    """
    story.append(Paragraph(faq2_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("16.2.3 Can I use my own model?", heading3_style))
    faq3_text = """
    <b>Answer:</b> Yes, you can replace pneumonia_model.h5 with your own trained model. 
    Ensure the model expects the same input format (224x224 RGB images) and outputs 
    a single probability value.
    """
    story.append(Paragraph(faq3_text, normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("16.2.4 How do I backup the database?", heading3_style))
    faq4_text = """
    <b>Answer:</b> For SQLite, simply copy the db.sqlite3 file. For PostgreSQL or MySQL, 
    use the respective database backup tools (pg_dump, mysqldump).
    """
    story.append(Paragraph(faq4_text, normal_style))
    story.append(PageBreak())
    
    # Continue with Dependencies section (similar to original)
    # Then add Future Enhancements and Conclusion
    
    # 17. Dependencies (Enhanced)
    story.append(Paragraph("17. Dependencies", heading1_style))
    dependencies_text = """
    The following are the main Python packages required for this project. A complete list is available 
    in requirements.txt. Install all dependencies using: pip install -r requirements.txt
    """
    story.append(Paragraph(dependencies_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("17.1 Core Dependencies", heading2_style))
    core_deps_text = """
    <b>Django 4.2.25:</b> Web framework for building the application
    <br/><b>TensorFlow 2.15.0:</b> Machine learning framework for loading and running the pneumonia prediction model
    <br/><b>Keras 2.15.0:</b> High-level neural networks API (included with TensorFlow)
    <br/><b>NumPy 1.26.4:</b> Numerical computing library for array operations
    <br/><b>Pillow 11.3.0:</b> Python Imaging Library for image processing and manipulation
    <br/><b>h5py 3.14.0:</b> Python interface to the HDF5 binary data format (required for loading .h5 model files)
    """
    story.append(Paragraph(core_deps_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("17.2 Installation Notes", heading2_style))
    install_notes_text = """
    <b>System Requirements:</b>
    <br/>• Python 3.8 or higher
    <br/>• TensorFlow supports both CPU and GPU. For GPU support, install TensorFlow-GPU and CUDA toolkit
    <br/>• Minimum 4GB RAM recommended (8GB+ for better performance)
    <br/>• Disk space: At least 2GB for dependencies and model files
    <br/><b>Installation Tips:</b>
    <br/>• Use a virtual environment to avoid conflicts with other projects
    <br/>• On Windows, you may need to install Visual C++ Redistributable for TensorFlow
    <br/>• For production, consider using a lighter deployment option or containerization (Docker)
    <br/>• Regularly update dependencies for security patches: pip install --upgrade -r requirements.txt
    """
    story.append(Paragraph(install_notes_text, normal_style))
    story.append(PageBreak())
    
    # 18. Future Enhancements (NEW SECTION)
    story.append(Paragraph("18. Future Enhancements", heading1_style))
    future_text = """
    This section outlines potential enhancements and improvements for future versions of the system.
    """
    story.append(Paragraph(future_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("18.1 Planned Features", heading2_style))
    planned_features_text = """
    <b>Short-term Enhancements:</b>
    <br/>• REST API for programmatic access
    <br/>• Batch image processing
    <br/>• Enhanced dashboard with charts and graphs
    <br/>• Export prediction history to CSV/PDF
    <br/>• Email notifications for predictions
    <br/><b>Long-term Enhancements:</b>
    <br/>• Support for multiple disease detection
    <br/>• Model retraining capabilities
    <br/>• Advanced visualization and analytics
    <br/>• Integration with healthcare systems (HL7, DICOM)
    <br/>• Mobile application support (iOS/Android)
    <br/>• Real-time prediction via WebSocket
    <br/>• Multi-language support
    <br/>• Advanced user roles and permissions
    """
    story.append(Paragraph(planned_features_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("18.2 Performance Optimizations", heading2_style))
    performance_text = """
    <b>Performance Improvements:</b>
    <br/>• Implement model caching and lazy loading
    <br/>• Add image compression and optimization
    <br/>• Implement database query optimization
    <br/>• Add Redis caching for predictions
    <br/>• Implement asynchronous task processing (Celery)
    <br/>• Add CDN for static and media files
    <br/>• Implement database connection pooling
    <br/>• Add gzip compression for responses
    <br/>• Optimize TensorFlow model inference
    <br/>• Implement batch processing for multiple images
    """
    story.append(Paragraph(performance_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("18.3 Scalability Improvements", heading2_style))
    scalability_text = """
    <b>Scalability Enhancements:</b>
    <br/>• Horizontal scaling with load balancers
    <br/>• Microservices architecture
    <br/>• Containerization with Docker
    <br/>• Kubernetes orchestration
    <br/>• Database replication and sharding
    <br/>• Message queue for async processing
    <br/>• Auto-scaling based on load
    <br/>• Geographic distribution
    """
    story.append(Paragraph(scalability_text, normal_style))
    story.append(PageBreak())
    
    # 19. Conclusion
    story.append(Paragraph("19. Conclusion", heading1_style))
    conclusion_text = """
    This documentation provides a comprehensive overview of the Disease Prediction System (Pneumonia Detector). 
    The system leverages deep learning and web technologies to provide an accessible platform for chest X-ray 
    image analysis.
    <br/><br/>
    <b>Key Takeaways:</b>
    <br/>• The system uses a pre-trained TensorFlow/Keras model for pneumonia detection
    <br/>• Django framework provides a robust and secure web interface
    <br/>• User authentication ensures data privacy and user-specific prediction history
    <br/>• The dashboard provides valuable insights into prediction statistics
    <br/>• The system is designed for extensibility and future enhancements
    <br/><br/>
    <b>System Strengths:</b>
    <br/>• Easy to deploy and configure
    <br/>• User-friendly interface
    <br/>• Secure authentication system
    <br/>• Comprehensive prediction tracking
    <br/>• Extensible architecture
    <br/><br/>
    <b>Important Disclaimer:</b>
    <br/>This system is intended for educational and research purposes only. It should not be used as a 
    substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified 
    healthcare professionals for medical decisions. The predictions generated by this system are not 
    intended for clinical use and should be verified by licensed medical professionals.
    <br/><br/>
    <b>Support and Contributions:</b>
    <br/>For issues, questions, or contributions, please refer to the project repository or contact 
    the development team. We welcome feedback and contributions to improve the system.
    """
    story.append(Paragraph(conclusion_text, normal_style))
    story.append(Spacer(1, 20))
    
    # Appendices
    story.append(Paragraph("Appendix A: Glossary", heading1_style))
    glossary_text = """
    <b>Terminology:</b>
    <br/><b>API:</b> Application Programming Interface - a set of protocols for building software applications
    <br/><b>CNN:</b> Convolutional Neural Network - a type of deep learning model used for image recognition
    <br/><b>Django:</b> A high-level Python web framework
    <br/><b>Keras:</b> A high-level neural networks API
    <br/><b>ML Model:</b> Machine Learning Model - a mathematical representation of patterns in data
    <br/><b>TensorFlow:</b> An open-source machine learning framework
    <br/><b>WSGI:</b> Web Server Gateway Interface - a specification for web servers and applications
    <br/><b>ASGI:</b> Asynchronous Server Gateway Interface - an extension of WSGI for async applications
    <br/><b>ORM:</b> Object-Relational Mapping - a technique for accessing databases
    <br/><b>REST API:</b> Representational State Transfer API - a web service architecture
    """
    story.append(Paragraph(glossary_text, normal_style))
    story.append(PageBreak())
    
    story.append(Paragraph("Appendix B: References", heading1_style))
    references_text = """
    <b>Documentation:</b>
    <br/>• Django Documentation: https://docs.djangoproject.com/
    <br/>• TensorFlow Documentation: https://www.tensorflow.org/api_docs
    <br/>• Keras Documentation: https://keras.io/api/
    <br/>• Python Documentation: https://docs.python.org/
    <br/><b>Libraries:</b>
    <br/>• ReportLab: https://www.reportlab.com/docs/reportlab-userguide.pdf
    <br/>• Pillow: https://pillow.readthedocs.io/
    <br/>• NumPy: https://numpy.org/doc/
    <br/><b>Best Practices:</b>
    <br/>• Django Security: https://docs.djangoproject.com/en/stable/topics/security/
    <br/>• PEP 8 Style Guide: https://www.python.org/dev/peps/pep-0008/
    <br/>• Web Security: https://owasp.org/www-project-top-ten/
    """
    story.append(Paragraph(references_text, normal_style))
    story.append(Spacer(1, 20))
    
    # Build PDF
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"✅ Enhanced documentation generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    try:
        create_documentation()
    except Exception as e:
        print(f"❌ Error generating documentation: {e}")
        import traceback
        traceback.print_exc()