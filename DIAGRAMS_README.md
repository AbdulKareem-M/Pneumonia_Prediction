# Diagrams for Pneumonia Prediction Project

This folder contains all the diagrams needed for your project review: System Architecture, Use Case Diagram, and Workflow Diagram.

## Quick Start

### Option 1: View in Browser (Easiest)
1. Open `view_diagrams.html` in any web browser
2. All three diagrams will be displayed interactively
3. You can take screenshots or use browser print-to-PDF

### Option 2: Use Mermaid Live Editor
1. Go to https://mermaid.live
2. Open the `.mmd` files from the `diagrams/` folder:
   - `diagrams/system_architecture.mmd`
   - `diagrams/use_case.mmd`
   - `diagrams/workflow.mmd`
3. Copy and paste the content into mermaid.live
4. Export as PNG/SVG from there

### Option 3: Use Draw.io
1. Read `diagram_descriptions.md` for detailed text descriptions
2. Go to https://app.diagrams.net
3. Recreate the diagrams using the descriptions provided

## Files Included

1. **view_diagrams.html** - Interactive HTML file with all diagrams (open in browser)
2. **diagram_descriptions.md** - Detailed text descriptions for manual creation
3. **diagrams/system_architecture.mmd** - Mermaid code for system architecture
4. **diagrams/use_case.mmd** - Mermaid code for use case diagram
5. **diagrams/workflow.mmd** - Mermaid code for workflow diagram

## Diagram Details

### 1. System Architecture Diagram
Shows the layered architecture:
- User Layer (Browser)
- Frontend Layer (Django Templates)
- Backend Layer (Django Framework)
- ML Processing Layer (TensorFlow/Keras)
- Data Storage Layer (SQLite + Media Files)

### 2. Use Case Diagram
Shows actors and their interactions:
- **Clinician**: Register, Login, Upload X-ray, View Results, View Dashboard
- **Admin**: Manage Users, View All Predictions, System Monitoring, Admin Panel

### 3. Workflow Diagram
Shows the complete process flow:
- User authentication
- Image upload and validation
- Image preprocessing
- Model inference
- Result calculation and storage
- Display and dashboard update

## For Project Review

These diagrams demonstrate:
- ✅ Clear system architecture
- ✅ User interactions (use cases)
- ✅ Complete workflow from upload to results
- ✅ Technical implementation details

## Tips for Presentation

1. **System Architecture**: Emphasize the separation of concerns (layers)
2. **Use Case Diagram**: Highlight primary user (Clinician) vs Admin roles
3. **Workflow Diagram**: Walk through the prediction process step-by-step

## Exporting for Documentation

- **From mermaid.live**: Use the export button (PNG/SVG)
- **From HTML**: Right-click diagram → Save image, or use browser screenshot
- **For PDF**: Use browser print-to-PDF on `view_diagrams.html`

Good luck with your project review! 🎉

