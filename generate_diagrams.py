"""
Script to generate System Architecture, Use Case, and Workflow diagrams
for the Pneumonia Prediction Project.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.patches as patches
from matplotlib.patches import ConnectionPatch
import numpy as np

def create_system_architecture_diagram():
    """Create System Architecture Diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(5, 11.5, 'System Architecture Diagram', 
            ha='center', va='center', fontsize=20, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
    
    # Frontend Layer
    frontend_box = FancyBboxPatch((1, 8.5), 8, 1.5, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='black', facecolor='#e3f2fd', linewidth=2)
    ax.add_patch(frontend_box)
    ax.text(5, 9.5, 'FRONTEND LAYER', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    ax.text(5, 9, 'Django Templates (HTML/CSS/JavaScript)\n' +
            '• Login/Signup Pages\n' +
            '• Image Upload Interface\n' +
            '• Results Display\n' +
            '• Dashboard View', 
            ha='center', va='center', fontsize=10)
    
    # Backend Layer - Django
    backend_box = FancyBboxPatch((1, 6), 8, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='black', facecolor='#c8e6c9', linewidth=2)
    ax.add_patch(backend_box)
    ax.text(5, 7, 'BACKEND LAYER (Django Framework)', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    ax.text(5, 6.5, '• Views (upload_and_predict, dashboard, signup)\n' +
            '• Forms (UploadImageForm)\n' +
            '• URL Routing\n' +
            '• Authentication & Authorization', 
            ha='center', va='center', fontsize=10)
    
    # ML Processing Layer
    ml_box = FancyBboxPatch((1, 3.5), 8, 1.5, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='black', facecolor='#fff9c4', linewidth=2)
    ax.add_patch(ml_box)
    ax.text(5, 4.5, 'ML PROCESSING LAYER', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    ax.text(5, 4, 'TensorFlow/Keras Model\n' +
            '• Image Preprocessing (resize, normalize)\n' +
            '• CNN Inference (pneumonia_model.h5)\n' +
            '• Prediction Probability Calculation', 
            ha='center', va='center', fontsize=10)
    
    # Data Storage Layer
    storage_box = FancyBboxPatch((1, 1), 8, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='black', facecolor='#f8bbd0', linewidth=2)
    ax.add_patch(storage_box)
    ax.text(5, 2, 'DATA STORAGE LAYER', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    ax.text(5, 1.5, 'SQLite Database (Predictions Table)\n' +
            'Media Storage (Uploaded X-ray Images)', 
            ha='center', va='center', fontsize=10)
    
    # Arrows showing data flow
    arrow1 = FancyArrowPatch((5, 8.5), (5, 7.5), 
                            arrowstyle='->', mutation_scale=20, 
                            color='red', linewidth=2)
    ax.add_patch(arrow1)
    ax.text(5.5, 8, 'HTTP Request', fontsize=9, color='red', fontweight='bold')
    
    arrow2 = FancyArrowPatch((5, 6), (5, 5), 
                            arrowstyle='->', mutation_scale=20, 
                            color='blue', linewidth=2)
    ax.add_patch(arrow2)
    ax.text(5.5, 5.5, 'Image Processing', fontsize=9, color='blue', fontweight='bold')
    
    arrow3 = FancyArrowPatch((5, 3.5), (5, 2.5), 
                            arrowstyle='->', mutation_scale=20, 
                            color='green', linewidth=2)
    ax.add_patch(arrow3)
    ax.text(5.5, 3, 'Save Results', fontsize=9, color='green', fontweight='bold')
    
    # User
    user_circle = Circle((5, 10.5), 0.3, color='orange', ec='black', linewidth=2)
    ax.add_patch(user_circle)
    ax.text(5, 10.5, 'U', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(5, 11.2, 'User/Clinician', ha='center', va='center', fontsize=10, fontweight='bold')
    
    user_arrow = FancyArrowPatch((5, 10.2), (5, 9.5), 
                                arrowstyle='->', mutation_scale=15, 
                                color='orange', linewidth=1.5)
    ax.add_patch(user_arrow)
    
    plt.tight_layout()
    plt.savefig('system_architecture_diagram.png', dpi=300, bbox_inches='tight')
    print("✅ System Architecture Diagram saved as 'system_architecture_diagram.png'")
    plt.close()


def create_use_case_diagram():
    """Create Use Case Diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Use Case Diagram', 
            ha='center', va='center', fontsize=20, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
    
    # System Boundary
    system_box = FancyBboxPatch((0.5, 1), 9, 7.5, 
                                boxstyle="round,pad=0.2", 
                                edgecolor='black', facecolor='#f0f0f0', 
                                linewidth=2, linestyle='--')
    ax.add_patch(system_box)
    ax.text(5, 8.2, 'Pneumonia Prediction System', 
            ha='center', va='center', fontsize=16, fontweight='bold')
    
    # Actors
    # Clinician
    actor1_box = Rectangle((0.2, 3), 1.2, 2, 
                          edgecolor='black', facecolor='#e3f2fd', linewidth=2)
    ax.add_patch(actor1_box)
    ax.text(0.8, 4.5, 'Clinician', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax.text(0.8, 4, '(Primary User)', ha='center', va='center', fontsize=9)
    
    # Admin
    actor2_box = Rectangle((8.6, 3), 1.2, 2, 
                          edgecolor='black', facecolor='#c8e6c9', linewidth=2)
    ax.add_patch(actor2_box)
    ax.text(9.2, 4.5, 'Admin', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax.text(9.2, 4, '(System Admin)', ha='center', va='center', fontsize=9)
    
    # Use Cases for Clinician
    use_cases_clinician = [
        (2.5, 6.5, 'Register Account'),
        (2.5, 5.5, 'Login'),
        (2.5, 4.5, 'Upload X-ray Image'),
        (2.5, 3.5, 'View Prediction Results'),
        (2.5, 2.5, 'View Dashboard'),
    ]
    
    # Use Cases for Admin
    use_cases_admin = [
        (6.5, 6.5, 'Manage Users'),
        (6.5, 5.5, 'View All Predictions'),
        (6.5, 4.5, 'System Monitoring'),
        (6.5, 3.5, 'Access Admin Panel'),
    ]
    
    # Draw use case ovals
    for x, y, label in use_cases_clinician:
        oval = FancyBboxPatch((x-0.8, y-0.25), 1.6, 0.5, 
                              boxstyle="round,pad=0.05", 
                              edgecolor='black', facecolor='#fff9c4', linewidth=1.5)
        ax.add_patch(oval)
        ax.text(x, y, label, ha='center', va='center', fontsize=9)
    
    for x, y, label in use_cases_admin:
        oval = FancyBboxPatch((x-0.8, y-0.25), 1.6, 0.5, 
                              boxstyle="round,pad=0.05", 
                              edgecolor='black', facecolor='#f8bbd0', linewidth=1.5)
        ax.add_patch(oval)
        ax.text(x, y, label, ha='center', va='center', fontsize=9)
    
    # Draw associations (lines from actors to use cases)
    # Clinician associations
    for x, y, _ in use_cases_clinician:
        line = ConnectionPatch((1.4, 4), (x-0.8, y), "data", "data",
                              arrowstyle='->', mutation_scale=15, 
                              color='blue', linewidth=1.5)
        ax.add_patch(line)
    
    # Admin associations
    for x, y, _ in use_cases_admin:
        line = ConnectionPatch((8.6, 4), (x+0.8, y), "data", "data",
                              arrowstyle='->', mutation_scale=15, 
                              color='green', linewidth=1.5)
        ax.add_patch(line)
    
    plt.tight_layout()
    plt.savefig('use_case_diagram.png', dpi=300, bbox_inches='tight')
    print("✅ Use Case Diagram saved as 'use_case_diagram.png'")
    plt.close()


def create_workflow_diagram():
    """Create Workflow/Process Flow Diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Title
    ax.text(5, 15.5, 'Workflow Diagram - Pneumonia Prediction Process', 
            ha='center', va='center', fontsize=18, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
    
    # Process steps
    steps = [
        (5, 14, 'Start: User Access', '#e3f2fd'),
        (5, 13, 'User Registration/Login', '#c8e6c9'),
        (5, 12, 'Navigate to Upload Page', '#fff9c4'),
        (5, 11, 'Select & Upload X-ray Image', '#f8bbd0'),
        (5, 10, 'Image Saved to Media Storage', '#e1bee7'),
        (5, 9, 'Image Preprocessing\n(Resize to 224x224, Normalize)', '#b2dfdb'),
        (5, 8, 'Load Trained CNN Model', '#c5cae9'),
        (5, 7, 'Model Inference\n(Predict Pneumonia)', '#ffccbc'),
        (5, 6, 'Calculate Probability & Label', '#d1c4e9'),
        (5, 5, 'Save Prediction to Database', '#b39ddb'),
        (5, 4, 'Display Results to User', '#90caf9'),
        (5, 3, 'Update Dashboard Statistics', '#81c784'),
        (5, 2, 'End: User Reviews Results', '#e3f2fd'),
    ]
    
    # Draw process boxes
    for i, (x, y, label, color) in enumerate(steps):
        box = FancyBboxPatch((x-1.5, y-0.4), 3, 0.8, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='black', facecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', 
                fontsize=10, fontweight='bold')
        
        # Add step number
        circle = Circle((x-1.8, y), 0.15, color='white', 
                       ec='black', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(x-1.8, y, str(i+1), ha='center', va='center', 
                fontsize=8, fontweight='bold')
    
    # Draw arrows between steps
    for i in range(len(steps) - 1):
        y1 = steps[i][1] - 0.4
        y2 = steps[i+1][1] + 0.4
        arrow = FancyArrowPatch((5, y1), (5, y2), 
                               arrowstyle='->', mutation_scale=20, 
                               color='red', linewidth=2)
        ax.add_patch(arrow)
    
    # Add decision point (optional)
    decision_y = 6.5
    diamond = patches.RegularPolygon((5, decision_y), 4, radius=0.4, 
                                     orientation=np.pi/4,
                                     edgecolor='black', facecolor='#ffeb3b', 
                                     linewidth=2)
    ax.add_patch(diamond)
    ax.text(5, decision_y, 'Prob > 0.5?', ha='center', va='center', 
            fontsize=9, fontweight='bold')
    
    # Add alternative paths
    ax.text(7, decision_y, 'Normal', ha='left', va='center', 
            fontsize=9, color='green', fontweight='bold')
    ax.text(3, decision_y, 'Pneumonia', ha='right', va='center', 
            fontsize=9, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('workflow_diagram.png', dpi=300, bbox_inches='tight')
    print("✅ Workflow Diagram saved as 'workflow_diagram.png'")
    plt.close()


def main():
    """Generate all diagrams"""
    print("Generating diagrams for Pneumonia Prediction Project...")
    print("-" * 50)
    
    try:
        create_system_architecture_diagram()
        create_use_case_diagram()
        create_workflow_diagram()
        
        print("-" * 50)
        print("✅ All diagrams generated successfully!")
        print("\nGenerated files:")
        print("  1. system_architecture_diagram.png")
        print("  2. use_case_diagram.png")
        print("  3. workflow_diagram.png")
        
    except Exception as e:
        print(f"❌ Error generating diagrams: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

