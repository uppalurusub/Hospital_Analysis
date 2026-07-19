# 🏥 Hospital Analysis System

A comprehensive **Hospital Analytics Platform** built using **FastAPI (Python)** and **React + TypeScript** for analyzing healthcare data, monitoring hospital performance, predicting patient outcomes, and providing executive dashboards.

The system helps hospitals, healthcare providers, administrators, analysts, and researchers gain actionable insights through interactive dashboards, predictive analytics, clinical risk analysis, financial reporting, and population health management.

---

# 📋 Table of Contents

- Project Overview
- Features
- System Architecture
- Technology Stack
- Project Structure
- Backend
- Frontend
- Installation
- Running the Project
- API Modules
- Data Sources
- Predictive Analytics
- Visualizations
- Future Enhancements
- Contributing
- License

---

# 📖 Project Overview

The Hospital Analysis System integrates healthcare datasets and applies descriptive, diagnostic, predictive, and executive analytics to provide insights into hospital operations.

The platform includes:

- Patient Analytics
- Disease Analytics
- Clinical Risk Assessment
- Financial Analytics
- Executive Dashboard
- Population Health Analytics
- Readmission Prediction
- Mortality Prediction
- ICU Prediction
- Length of Stay Prediction
- Medication Analytics
- Cost Analysis

The project follows a modular enterprise architecture separating:

- API Layer
- Business Logic
- Services
- Visualization Layer
- React Dashboard

---

# 🚀 Features

## Clinical Analytics

- Population Health Dashboard
- Disease Prevalence Analysis
- Clinical Risk Analysis
- Patient Outcomes
- Readmission Analysis
- Mortality Analysis
- ICU Analysis
- Length of Stay Analysis

---

## Financial Analytics

- Hospital Revenue
- Treatment Cost Analysis
- Cost Distribution
- Department Cost
- Financial KPIs
- Resource Utilization

---

## Executive Dashboard

Provides executive-level KPIs including:

- Total Patients
- Total Admissions
- Revenue
- Average Length of Stay
- ICU Admissions
- Readmission Rate
- Mortality Rate
- Occupancy Rate
- Clinical Risk Score
- Operational KPIs

---

## Predictive Analytics

Machine Learning based predictions including:

- Readmission Prediction
- Mortality Prediction
- ICU Prediction
- Length of Stay Prediction
- Risk Prediction

---

## Interactive Dashboard

Frontend includes:

- KPI Cards
- Charts
- Tables
- Markdown Reports
- Interactive Visualizations
- Dynamic API Integration

---

# 🏗 System Architecture

```
                    React + TypeScript UI
                             │
                             │ REST API
                             ▼
                    FastAPI Backend
                             │
        ┌────────────────────────────────┐
        │             Routers            │
        └────────────────────────────────┘
                             │
                             ▼
        ┌────────────────────────────────┐
        │            Services            │
        └────────────────────────────────┘
                             │
                             ▼
        ┌────────────────────────────────┐
        │       Business Implementations │
        └────────────────────────────────┘
                             │
             ┌───────────────┴───────────────┐
             ▼                               ▼
       CSV Healthcare Data           Visualization Layer
```

---

# 💻 Technology Stack

## Backend

- Python
- FastAPI
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Plotly
- MLflow
- Uvicorn

---

## Frontend

- React 19
- TypeScript
- Vite
- Axios
- React Router
- Recharts
- React Markdown
- Lucide Icons

---

# 📂 Project Structure

```
Hospital_Analysis/

│
├── backend/
│   ├── hospital-analysis-python-app/
│   │
│   ├── routers/
│   ├── services/
│   ├── implementations/
│   ├── visualizations/
│   ├── utils/
│   ├── models/
│   ├── config/
│   ├── outputs/
│   └── main.py
│
├── ui/
│   └── reactjs/
│       └── hospital-analysis-react-app/
│           ├── src/
│           │   ├── api/
│           │   ├── components/
│           │   ├── pages/
│           │   ├── hooks/
│           │   ├── types/
│           │   └── App.tsx
│           └── package.json
│
└── data/
```

---

# ⚙ Backend

The backend is developed using **FastAPI** and exposes REST APIs for healthcare analytics.

## Main Components

### Routers

- Healthcare Router
- Disease Router
- Population Router
- Clinical Risk Router
- Outcomes Router
- Financial Router
- Predictive Router
- Executive Dashboard Router
- Readmission Router
- Mortality Router
- ICU Router
- LOS Router
- Medication Router
- Cost Router

---

### Services

Each router communicates with a dedicated service layer responsible for business orchestration.

---

### Implementations

Contains core analytics logic:

- Data Processing
- Feature Engineering
- Statistical Analysis
- Machine Learning
- KPI Generation
- Chart Generation

---

### Utilities

- Data Loader
- JSON Sanitizer
- Validators
- Safe Float Conversion
- Chart Utilities

---

# 🎨 Frontend

Built using **React + TypeScript + Vite**

Features include:

- Dashboard
- KPI Cards
- Charts
- Data Tables
- Markdown Reports
- Responsive UI
- REST API Integration

Reusable Components:

- DashboardView
- ChartView
- DataTable
- KPI Card
- Markdown Card

---

# 📊 Data Sources

Healthcare datasets include:

- Patients
- Diagnoses
- Lab Results
- Medications
- Outcomes

CSV files are located under:

```
backend/data/
```

---

# 📡 API Modules

| Module | Description |
|---------|-------------|
| Healthcare | General Analytics |
| Population | Population Health |
| Disease | Disease Prevalence |
| Clinical Risk | Clinical Risk Analysis |
| Outcomes | Patient Outcomes |
| Financial | Financial Analytics |
| Executive | Executive Dashboard |
| Predictive | Prediction Models |
| Readmission | Readmission Analytics |
| Mortality | Mortality Analytics |
| ICU | ICU Analytics |
| LOS | Length of Stay |
| Medication | Medication Analytics |
| Cost | Cost Analytics |

---

# 📈 Visualizations

The application generates:

- Bar Charts
- Line Charts
- Pie Charts
- KPI Cards
- Heatmaps
- Trend Charts
- Financial Charts
- Clinical Dashboards

Generated charts are stored in:

```
outputs/
```

---

# 🤖 Machine Learning

Predictive modules include:

- Readmission Prediction
- Mortality Prediction
- ICU Prediction
- Length of Stay Prediction
- Risk Prediction

The system also supports:

- Feature Engineering
- Model Evaluation
- MLflow Tracking
- Prediction APIs

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Hospital_Analysis.git

cd Hospital_Analysis
```

---

# Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
cd hospital-analysis-python-app

uvicorn main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger UI

```
http://localhost:8000/docs
```

---

# Frontend Setup

Navigate to React application

```bash
cd ui/reactjs/hospital-analysis-react-app
```

Install packages

```bash
npm install
```

Run application

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# 🔄 Application Flow

```
React Dashboard

      │

Axios REST Calls

      │

FastAPI Router

      │

Service Layer

      │

Business Implementation

      │

CSV Data Processing

      │

Analytics Results

      │

JSON Response

      │

Dashboard Rendering
```

---

# 📊 Key Analytics

The system provides insights into:

- Patient Demographics
- Disease Distribution
- Clinical Risk
- Population Health
- Hospital Revenue
- Cost Analysis
- ICU Utilization
- Readmissions
- Mortality
- Average Length of Stay
- Executive KPIs

---

# 🔮 Future Enhancements

- PostgreSQL Integration
- Authentication & Authorization
- Role-Based Access Control
- Docker Support
- Kubernetes Deployment
- Azure/AWS Deployment
- Real-Time Analytics
- PDF Report Generation
- AI-Based Clinical Recommendations
- Time Series Forecasting
- Advanced ML Models

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Create a Pull Request

---

# 📜 License

This project is intended for educational, research, and healthcare analytics purposes.

---

# 👨‍💻 Author

**Hospital Analysis System**

Built using:

- FastAPI
- Python
- React
- TypeScript
- Machine Learning
- Healthcare Analytics

Designed for healthcare organizations, researchers, hospital administrators, and data analysts.