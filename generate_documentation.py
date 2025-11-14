"""
Script to generate PDF documentation for the Disease Prediction (Pneumonia Detector) project.
"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted
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
    """Generate the PDF documentation."""
    # Create PDF file
    filename = "Disease_Prediction_Project_Documentation.pdf"
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
    story.append(Paragraph("Project Documentation", ParagraphStyle(
        'Subtitle2',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#64748b'),
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
    and implementation details.
    """
    story.append(Paragraph(abstract_text, normal_style))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Table of Contents", heading1_style))
    toc_items = [
        "1. Introduction",
        "2. Project Structure",
        "3. Core Module (disease_prediction)",
        "4. Pneumonia Predictor Module",
        "5. Authentication Module",
        "6. Database Models",
        "7. URL Routing and Views",
        "8. Templates and User Interface",
        "9. Installation and Setup",
        "10. Usage Instructions",
        "11. API Endpoints",
        "12. Dependencies"
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
    
    <b>Key Features:</b>
    <br/>• User authentication and authorization
    <br/>• Image upload and preprocessing
    <br/>• Real-time pneumonia prediction using deep learning
    <br/>• Prediction history and statistics dashboard
    <br/>• User-friendly web interface
    <br/>• Secure file handling and storage
    """
    story.append(Paragraph(intro_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("1.1 Technology Stack", heading2_style))
    tech_stack_text = """
    <b>Backend Framework:</b> Django 4.2.25
    <br/><b>Machine Learning:</b> TensorFlow 2.15.0, Keras 2.15.0
    <br/><b>Database:</b> SQLite3
    <br/><b>Image Processing:</b> Pillow 11.3.0, NumPy 1.26.4
    <br/><b>Frontend:</b> HTML5, CSS3, JavaScript
    <br/><b>Server:</b> Django Development Server (WSGI/ASGI)
    """
    story.append(Paragraph(tech_stack_text, normal_style))
    story.append(PageBreak())
    
    # 2. Project Structure
    story.append(Paragraph("2. Project Structure", heading1_style))
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
│   ├── templates/               # HTML templates
│   │   ├── base.html
│   │   ├── upload.html
│   │   ├── dashboard.html
│   │   └── registration/
│   │       ├── login.html
│   │       └── signup.html
│   └── models/                  # ML model storage
│       └── pneumonia_model.h5
├── media/                       # Uploaded media files
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django management script
└── requirements.txt             # Python dependencies
    """
    story.append(Preformatted(structure_code, code_style))
    story.append(PageBreak())
    
    # 3. Core Module
    story.append(Paragraph("3. Core Module (disease_prediction)", heading1_style))
    story.append(Paragraph("The core module contains the main Django project configuration.", normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("3.1 settings.py", heading2_style))
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
    
    story.append(Paragraph("3.2 urls.py", heading2_style))
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
    
    story.append(Paragraph("3.3 wsgi.py and asgi.py", heading2_style))
    wsgi_text = """
    <b>wsgi.py:</b> Web Server Gateway Interface configuration for deployment with WSGI servers 
    (e.g., Gunicorn, uWSGI)
    <br/><b>asgi.py:</b> Asynchronous Server Gateway Interface configuration for deployment with 
    ASGI servers (e.g., Daphne, Uvicorn) supporting WebSockets and async features
    """
    story.append(Paragraph(wsgi_text, normal_style))
    story.append(PageBreak())
    
    # 4. Pneumonia Predictor Module
    story.append(Paragraph("4. Pneumonia Predictor Module", heading1_style))
    story.append(Paragraph("The pneumonia_predictor module is the main application containing the core functionality.", normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.1 views.py", heading2_style))
    views_text = """
    The views.py file contains all view functions that handle HTTP requests:
    """
    story.append(Paragraph(views_text, normal_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("4.1.1 predict_pneumonia()", heading3_style))
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
    
    story.append(Paragraph("4.1.2 upload_and_predict()", heading3_style))
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
    
    story.append(Paragraph("4.1.3 dashboard()", heading3_style))
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
    
    story.append(Paragraph("4.1.4 signup()", heading3_style))
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
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.2 models.py", heading2_style))
    models_text = """
    The models.py file defines the database models:
    """
    story.append(Paragraph(models_text, normal_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("4.2.1 Prediction Model", heading3_style))
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
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.3 forms.py", heading2_style))
    forms_text = """
    The forms.py file defines form classes for user input:
    """
    story.append(Paragraph(forms_text, normal_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("4.3.1 UploadImageForm", heading3_style))
    form_text = """
    <b>Form:</b> UploadImageForm
    <br/><b>Fields:</b>
    <br/>• image (ImageField): Field for uploading chest X-ray images
    <br/><b>Validation:</b> Django automatically validates that uploaded file is a valid image format
    <br/><b>Usage:</b> Used in upload_and_predict view for image upload functionality
    """
    story.append(Paragraph(form_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.4 admin.py", heading2_style))
    admin_text = """
    The admin.py file is used to register models with Django's admin interface. 
    Currently, no models are registered, but the Prediction model can be registered 
    for administrative management of prediction records.
    """
    story.append(Paragraph(admin_text, normal_style))
    story.append(PageBreak())
    
    # 5. Authentication Module
    story.append(Paragraph("5. Authentication Module", heading1_style))
    auth_text = """
    The application uses Django's built-in authentication system (django.contrib.auth) 
    for user management and authentication.
    """
    story.append(Paragraph(auth_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("5.1 Authentication Features", heading2_style))
    auth_features_text = """
    <b>User Registration:</b>
    <br/>• Custom signup view using UserCreationForm
    <br/>• Automatic login after successful registration
    <br/>• Password validation (minimum 8 characters, common password checks)
    <br/><b>User Login:</b>
    <br/>• Django's built-in login view
    <br/>• Session-based authentication
    <br/>• Redirects to upload page after login
    <br/><b>User Logout:</b>
    <br/>• Django's built-in logout view
    <br/>• Redirects to login page after logout
    <br/><b>Password Management:</b>
    <br/>• Password reset functionality (via Django's built-in views)
    <br/>• Password change functionality
    <br/><b>Access Control:</b>
    <br/>• @login_required decorator protects views
    <br/>• Unauthenticated users are redirected to login page
    """
    story.append(Paragraph(auth_features_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("5.2 Authentication URLs", heading2_style))
    auth_urls_text = """
    The following authentication URLs are available:
    <br/>• /accounts/login/ - User login page
    <br/>• /accounts/logout/ - User logout
    <br/>• /accounts/signup/ - User registration page
    <br/>• /accounts/password_reset/ - Password reset request
    <br/>• /accounts/password_reset/done/ - Password reset confirmation
    <br/>• /accounts/reset/<uidb64>/<token>/ - Password reset form
    <br/>• /accounts/reset/done/ - Password reset complete
    """
    story.append(Paragraph(auth_urls_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("5.3 User Model", heading2_style))
    user_model_text = """
    The application uses Django's default User model which includes:
    <br/>• username - Unique username for each user
    <br/>• password - Hashed password stored securely
    <br/>• email - User email address (optional)
    <br/>• first_name, last_name - User's name (optional)
    <br/>• is_active - Whether the user account is active
    <br/>• is_staff - Whether the user can access admin site
    <br/>• is_superuser - Whether the user has all permissions
    <br/>• date_joined - Account creation timestamp
    """
    story.append(Paragraph(user_model_text, normal_style))
    story.append(PageBreak())
    
    # 6. Database Models
    story.append(Paragraph("6. Database Models", heading1_style))
    db_text = """
    The application uses SQLite3 as the database (suitable for development and small deployments). 
    For production, consider using PostgreSQL or MySQL.
    """
    story.append(Paragraph(db_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("6.1 Database Schema", heading2_style))
    schema_text = """
    <b>Prediction Table:</b>
    <br/>• id (Primary Key, Auto-increment)
    <br/>• user_id (Foreign Key to User table)
    <br/>• image_name (VARCHAR 255)
    <br/>• label (VARCHAR 32)
    <br/>• probability (FLOAT)
    <br/>• created_at (DATETIME)
    <br/><b>Relationships:</b>
    <br/>• One User can have many Predictions (One-to-Many)
    <br/>• Predictions are cascade deleted when User is deleted
    """
    story.append(Paragraph(schema_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("6.2 Database Migrations", heading2_style))
    migrations_text = """
    Database migrations are stored in pneumonia_predictor/migrations/ directory.
    <br/><b>Initial Migration:</b> 0001_initial.py creates the Prediction table
    <br/><b>Running Migrations:</b> python manage.py migrate
    <br/><b>Creating Migrations:</b> python manage.py makemigrations
    """
    story.append(Paragraph(migrations_text, normal_style))
    story.append(PageBreak())
    
    # 7. URL Routing and Views
    story.append(Paragraph("7. URL Routing and Views", heading1_style))
    routing_text = """
    The application uses Django's URL routing system to map URLs to view functions.
    """
    story.append(Paragraph(routing_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("7.1 URL Patterns", heading2_style))
    url_table_data = [
        ['URL Pattern', 'View Function', 'Name', 'Requires Auth'],
        ['/admin/', 'admin.site.urls', 'admin', 'Yes (Staff)'],
        ['/', 'upload_and_predict', 'upload_and_predict', 'Yes'],
        ['/dashboard/', 'dashboard', 'dashboard', 'Yes'],
        ['/accounts/signup/', 'signup', 'signup', 'No'],
        ['/accounts/login/', 'django.contrib.auth.views.LoginView', 'login', 'No'],
        ['/accounts/logout/', 'django.contrib.auth.views.LogoutView', 'logout', 'No'],
        ['/media/<path>', 'serve media files', 'N/A', 'No']
    ]
    
    url_table = Table(url_table_data, colWidths=[2*inch, 2.5*inch, 1.5*inch, 1*inch])
    url_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8fafc')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#1f2937')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e5e7eb')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9fafb')])
    ]))
    story.append(url_table)
    story.append(PageBreak())
    
    # 8. Templates and User Interface
    story.append(Paragraph("8. Templates and User Interface", heading1_style))
    templates_text = """
    The application uses Django's template system with HTML templates located in 
    pneumonia_predictor/templates/ directory.
    """
    story.append(Paragraph(templates_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("8.1 Base Template (base.html)", heading2_style))
    base_template_text = """
    <b>Purpose:</b> Base template that all other templates extend
    <br/><b>Features:</b>
    <br/>• Responsive navigation bar with user authentication status
    <br/>• Links to Predict, Dashboard, Login, Logout, Sign Up
    <br/>• User badge showing current logged-in user
    <br/>• Modern CSS styling with gradient themes
    <br/>• Mobile-responsive design
    <br/>• Block system for title, content, extra_head, and extra_scripts
    """
    story.append(Paragraph(base_template_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("8.2 Upload Template (upload.html)", heading2_style))
    upload_template_text = """
    <b>Purpose:</b> Main page for uploading chest X-ray images and viewing predictions
    <br/><b>Features:</b>
    <br/>• Drag-and-drop file upload zone
    <br/>• Image preview before submission
    <br/>• Real-time prediction results display
    <br/>• Confidence meter visualization
    <br/>• Prediction label (Normal/Pneumonia) with color coding
    <br/>• Medical disclaimer notice
    <br/>• Responsive two-column layout (upload form + results panel)
    """
    story.append(Paragraph(upload_template_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("8.3 Dashboard Template (dashboard.html)", heading2_style))
    dashboard_template_text = """
    <b>Purpose:</b> Display prediction statistics and history
    <br/><b>Features:</b>
    <br/>• Statistics cards showing total predictions, pneumonia cases, normal cases
    <br/>• Recent predictions table with image thumbnails
    <br/>• Prediction labels with color-coded badges
    <br/>• Confidence scores and timestamps
    <br/>• User-specific prediction history
    <br/>• Information sidebar with usage tips
    <br/>• Responsive grid layout
    """
    story.append(Paragraph(dashboard_template_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("8.4 Authentication Templates", heading2_style))
    auth_templates_text = """
    <b>Login Template (registration/login.html):</b>
    <br/>• User login form with username and password fields
    <br/>• Error message display for invalid credentials
    <br/>• Link to signup page
    <br/>• Modern card-based design
    <br/><b>Signup Template (registration/signup.html):</b>
    <br/>• User registration form
    <br/>• Password validation requirements
    <br/>• Form error display
    <br/>• Link to login page
    <br/>• Automatic login after successful registration
    """
    story.append(Paragraph(auth_templates_text, normal_style))
    story.append(PageBreak())
    
    # 9. Installation and Setup
    story.append(Paragraph("9. Installation and Setup", heading1_style))
    installation_text = """
    Follow these steps to set up and run the Disease Prediction System:
    """
    story.append(Paragraph(installation_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("9.1 Prerequisites", heading2_style))
    prerequisites_text = """
    <b>Required Software:</b>
    <br/>• Python 3.8 or higher
    <br/>• pip (Python package installer)
    <br/>• Virtual environment (recommended)
    <br/>• TensorFlow-compatible system (CPU or GPU)
    """
    story.append(Paragraph(prerequisites_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("9.2 Installation Steps", heading2_style))
    install_steps_text = """
    <b>Step 1: Clone or Download Project</b>
    <br/>Download or clone the project to your local machine.
    <br/><b>Step 2: Create Virtual Environment</b>
    <br/>python -m venv venv
    <br/><b>Step 3: Activate Virtual Environment</b>
    <br/>Windows: venv\\Scripts\\activate
    <br/>Linux/Mac: source venv/bin/activate
    <br/><b>Step 4: Install Dependencies</b>
    <br/>pip install -r requirements.txt
    <br/><b>Step 5: Run Migrations</b>
    <br/>python manage.py migrate
    <br/><b>Step 6: Create Superuser (Optional)</b>
    <br/>python manage.py createsuperuser
    <br/>This allows you to access the Django admin interface.
    <br/><b>Step 7: Ensure Model File Exists</b>
    <br/>Make sure the pneumonia_model.h5 file is located in pneumonia_predictor/models/ directory.
    <br/>The model file is required for predictions to work.
    """
    story.append(Paragraph(install_steps_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("9.3 Running the Application", heading2_style))
    running_text = """
    <b>Start Development Server:</b>
    <br/>python manage.py runserver
    <br/>The application will be available at http://127.0.0.1:8000/
    <br/><b>Access Admin Interface:</b>
    <br/>Navigate to http://127.0.0.1:8000/admin/ and login with superuser credentials
    <br/><b>Stop Server:</b>
    <br/>Press Ctrl+C in the terminal to stop the development server
    <br/><b>Note:</b> The development server is not suitable for production. For production deployment, 
    use a proper WSGI/ASGI server like Gunicorn or uWSGI with a reverse proxy like Nginx.
    """
    story.append(Paragraph(running_text, normal_style))
    story.append(PageBreak())
    
    # 10. Usage Instructions
    story.append(Paragraph("10. Usage Instructions", heading1_style))
    usage_text = """
    This section provides step-by-step instructions for using the Disease Prediction System.
    """
    story.append(Paragraph(usage_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("10.1 User Registration", heading2_style))
    registration_usage_text = """
    <b>Step 1: Access Registration Page</b>
    <br/>Navigate to http://127.0.0.1:8000/accounts/signup/ or click the "Sign Up" link in the navigation bar.
    <br/><b>Step 2: Fill Registration Form</b>
    <br/>• Enter a unique username
    <br/>• Enter a secure password (minimum 8 characters)
    <br/>• Confirm the password
    <br/><b>Step 3: Submit Registration</b>
    <br/>Click the "Sign Up" button. Upon successful registration, you will be automatically logged in 
    and redirected to the upload page.
    """
    story.append(Paragraph(registration_usage_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("10.2 User Login", heading2_style))
    login_usage_text = """
    <b>Step 1: Access Login Page</b>
    <br/>Navigate to http://127.0.0.1:8000/accounts/login/ or click the "Login" link in the navigation bar.
    <br/><b>Step 2: Enter Credentials</b>
    <br/>• Enter your username
    <br/>• Enter your password
    <br/><b>Step 3: Submit Login</b>
    <br/>Click the "Login" button. Upon successful login, you will be redirected to the upload page.
    """
    story.append(Paragraph(login_usage_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("10.3 Making Predictions", heading2_style))
    prediction_usage_text = """
    <b>Step 1: Access Upload Page</b>
    <br/>Navigate to http://127.0.0.1:8000/ or click "Predict" in the navigation bar (requires login).
    <br/><b>Step 2: Upload Chest X-ray Image</b>
    <br/>• Click the upload area or drag and drop a chest X-ray image file
    <br/>• Supported formats: JPEG, PNG, GIF, BMP
    <br/>• Recommended image size: 224x224 pixels or larger (will be resized automatically)
    <br/><b>Step 3: View Prediction Results</b>
    <br/>After uploading, the system will:
    <br/>• Display the uploaded image
    <br/>• Show prediction label (Normal or Pneumonia)
    <br/>• Display confidence score (probability)
    <br/>• Show a visual confidence meter
    <br/><b>Step 4: Review Results</b>
    <br/>The prediction result is automatically saved to your account and can be viewed in the Dashboard.
    <br/><b>Important:</b> This tool is for educational/research purposes only. Always consult with 
    healthcare professionals for medical diagnoses.
    """
    story.append(Paragraph(prediction_usage_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("10.4 Viewing Dashboard", heading2_style))
    dashboard_usage_text = """
    <b>Step 1: Access Dashboard</b>
    <br/>Navigate to http://127.0.0.1:8000/dashboard/ or click "Dashboard" in the navigation bar (requires login).
    <br/><b>Step 2: View Statistics</b>
    <br/>The dashboard displays:
    <br/>• Total number of predictions made
    <br/>• Number of pneumonia cases detected
    <br/>• Number of normal cases detected
    <br/><b>Step 3: View Prediction History</b>
    <br/>• Scroll through your recent predictions (last 20)
    <br/>• View image thumbnails, prediction labels, confidence scores, and timestamps
    <br/>• Predictions are sorted by most recent first
    """
    story.append(Paragraph(dashboard_usage_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("10.5 User Logout", heading2_style))
    logout_usage_text = """
    <b>Step 1: Click Logout</b>
    <br/>Click the "Logout" link in the navigation bar.
    <br/><b>Step 2: Confirmation</b>
    <br/>You will be logged out and redirected to the login page. You must log in again to access 
    protected features.
    """
    story.append(Paragraph(logout_usage_text, normal_style))
    story.append(PageBreak())
    
    # 11. API Endpoints
    story.append(Paragraph("11. API Endpoints", heading1_style))
    api_text = """
    The application provides web-based endpoints (URLs) for accessing different features. 
    While this is not a REST API, the URL endpoints serve as the interface to the application.
    """
    story.append(Paragraph(api_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("11.1 Public Endpoints", heading2_style))
    public_endpoints_text = """
    <b>Login Page:</b> GET /accounts/login/
    <br/>• Purpose: Display user login form
    <br/>• Method: GET (display form), POST (submit credentials)
    <br/>• Authentication: Not required
    <br/><b>Registration Page:</b> GET /accounts/signup/
    <br/>• Purpose: Display user registration form
    <br/>• Method: GET (display form), POST (submit registration)
    <br/>• Authentication: Not required
    <br/><b>Password Reset:</b> GET /accounts/password_reset/
    <br/>• Purpose: Request password reset
    <br/>• Method: GET, POST
    <br/>• Authentication: Not required
    """
    story.append(Paragraph(public_endpoints_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("11.2 Protected Endpoints", heading2_style))
    protected_endpoints_text = """
    <b>Upload and Predict:</b> GET, POST /
    <br/>• Purpose: Upload chest X-ray image and get prediction
    <br/>• Method: GET (display form), POST (upload image and predict)
    <br/>• Authentication: Required (login_required decorator)
    <br/>• Parameters: image (file upload in POST request)
    <br/>• Returns: HTML page with prediction results
    <br/><b>Dashboard:</b> GET /dashboard/
    <br/>• Purpose: Display prediction statistics and history
    <br/>• Method: GET
    <br/>• Authentication: Required (login_required decorator)
    <br/>• Returns: HTML page with statistics and recent predictions
    <br/><b>Logout:</b> POST /accounts/logout/
    <br/>• Purpose: Log out current user
    <br/>• Method: POST
    <br/>• Authentication: Required
    <br/>• Returns: Redirects to login page
    <br/><b>Admin Interface:</b> GET /admin/
    <br/>• Purpose: Django admin interface for managing data
    <br/>• Method: GET, POST
    <br/>• Authentication: Required (staff user)
    """
    story.append(Paragraph(protected_endpoints_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("11.3 Media Files", heading2_style))
    media_endpoints_text = """
    <b>Media Files:</b> GET /media/<filename>
    <br/>• Purpose: Serve uploaded images
    <br/>• Method: GET
    <br/>• Authentication: Not required (in development)
    <br/>• Note: In production, configure proper media file serving through web server (Nginx, Apache)
    """
    story.append(Paragraph(media_endpoints_text, normal_style))
    story.append(PageBreak())
    
    # 12. Dependencies
    story.append(Paragraph("12. Dependencies", heading1_style))
    dependencies_text = """
    The following are the main Python packages required for this project. A complete list is available 
    in requirements.txt. Install all dependencies using: pip install -r requirements.txt
    """
    story.append(Paragraph(dependencies_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("12.1 Core Dependencies", heading2_style))
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
    
    story.append(Paragraph("12.2 Supporting Dependencies", heading2_style))
    supporting_deps_text = """
    <b>asgiref 3.10.0:</b> ASGI specification and utilities (Django dependency)
    <br/><b>sqlparse 0.5.3:</b> SQL parser for Django database operations
    <br/><b>tzdata 2025.2:</b> Timezone database for datetime operations
    <br/><b>MarkupSafe 3.0.3:</b> Safe string handling for templates
    <br/><b>Werkzeug 3.1.3:</b> WSGI utilities (used by Django development server)
    """
    story.append(Paragraph(supporting_deps_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("12.3 TensorFlow Dependencies", heading2_style))
    tf_deps_text = """
    TensorFlow requires several additional packages for proper functioning:
    <br/><b>protobuf 4.25.8:</b> Protocol buffers for serializing structured data
    <br/><b>grpcio 1.75.1:</b> gRPC library for communication
    <br/><b>flatbuffers 25.9.23:</b> Serialization library for efficient data storage
    <br/><b>tensorboard 2.15.2:</b> Visualization toolkit for TensorFlow (optional, for model training)
    <br/><b>gast 0.4.0:</b> Generic AST (Abstract Syntax Tree) for Python
    <br/><b>opt_einsum 3.4.0:</b> Optimized einsum function for tensor operations
    <br/><b>ml-dtypes 0.2.0:</b> Machine learning data types
    <br/><b>termcolor 3.1.0:</b> ANSI color formatting for terminal output
    """
    story.append(Paragraph(tf_deps_text, normal_style))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("12.4 Installation Notes", heading2_style))
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
    story.append(Spacer(1, 12))
    
    # Conclusion
    story.append(Paragraph("Conclusion", heading1_style))
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
    <br/><br/>
    <b>Future Enhancements:</b>
    <br/>• REST API for programmatic access
    <br/>• Support for multiple disease detection
    <br/>• Model retraining capabilities
    <br/>• Advanced visualization and analytics
    <br/>• Integration with healthcare systems
    <br/>• Mobile application support
    <br/><br/>
    <b>Important Disclaimer:</b>
    <br/>This system is intended for educational and research purposes only. It should not be used as a 
    substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified 
    healthcare professionals for medical decisions.
    """
    story.append(Paragraph(conclusion_text, normal_style))
    story.append(Spacer(1, 20))
    
    # Build PDF
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"✅ Documentation generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    try:
        create_documentation()
    except Exception as e:
        print(f"❌ Error generating documentation: {e}")
        import traceback
        traceback.print_exc()