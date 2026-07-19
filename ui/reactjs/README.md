# HealthSight — Healthcare Analytics Platform

HealthSight is a responsive, API-driven healthcare analytics dashboard built with **React**, **TypeScript**, **React Router**, **Axios**, and **Recharts**.

The application provides interactive analytics across healthcare cost, disease prevalence, ICU utilization, length of stay, medication adherence, mortality, population health, readmission, and clinical risk domains.

HealthSight consumes JSON analytics APIs from a FastAPI backend and dynamically transforms API responses into:

* KPI cards
* Pie charts
* Bar charts
* Responsive data tables
* Markdown analytics summaries
* React-native dashboard views
* Structured error and loading states

---

## Table of Contents

* [Overview](#overview)
* [Key Features](#key-features)
* [Technology Stack](#technology-stack)
* [Analytics Modules](#analytics-modules)
* [Project Structure](#project-structure)
* [Application Architecture](#application-architecture)
* [Dashboard Architecture](#dashboard-architecture)
* [API Integration](#api-integration)
* [Dashboard KPI Processing](#dashboard-kpi-processing)
* [Dynamic Response Rendering](#dynamic-response-rendering)
* [Chart Rendering](#chart-rendering)
* [Data Formatting](#data-formatting)
* [Routing](#routing)
* [Installation](#installation)
* [Environment Configuration](#environment-configuration)
* [Running the Application](#running-the-application)
* [Backend Requirements](#backend-requirements)
* [API Endpoint Resolution](#api-endpoint-resolution)
* [Error Handling](#error-handling)
* [Responsive Design](#responsive-design)
* [Adding a New Analytics Module](#adding-a-new-analytics-module)
* [Adding Dashboard Endpoints](#adding-dashboard-endpoints)
* [Component Reference](#component-reference)
* [Future Enhancements](#future-enhancements)

---

## Overview

HealthSight is designed as a frontend analytics layer for a healthcare analytics API platform.

The frontend does not hardcode analytics results. Instead, it requests healthcare metrics from backend REST APIs and intelligently determines how the returned JSON should be presented.

For example:

```json
{
  "average_cost": 12451.75,
  "total_cost": 2450000,
  "high_cost_patient_rate": 18.5
}
```

The application automatically renders primitive values as KPI cards.

Array-based responses such as:

```json
[
  {
    "age_group": "18-30",
    "average_cost": 4250
  },
  {
    "age_group": "31-45",
    "average_cost": 6750
  }
]
```

can automatically be rendered as charts and detailed tables.

This architecture minimizes module-specific UI code and enables the frontend to support multiple analytics APIs using reusable visualization components.

---

## Key Features

### API-Driven Healthcare Analytics

All analytics data is loaded dynamically from REST API endpoints.

### React-Native Dashboard KPIs

The `/dashboard-kpis` option does not directly display a FastAPI JSON response.

Instead, React loads multiple analytics endpoints and composes a visual dashboard using:

* KPI cards
* Charts
* Tables
* Markdown summaries

### Dynamic JSON Visualization

The UI analyzes API response structures and automatically determines the appropriate visual representation.

### KPI Cards

Primitive values such as numbers, percentages, rates, costs, and boolean indicators are displayed as structured KPI cards.

### Recharts Visualizations

Healthcare analytics are displayed using:

* Pie charts
* Horizontal bar charts
* Vertical bar charts

### Responsive Data Tables

Detailed analytics results are displayed using horizontally scrollable responsive tables.

### Markdown Rendering

Text-based analytics summaries can be returned by APIs and displayed as formatted Markdown.

### API Prefix Fallback

The application supports backend APIs configured with or without an `/api` prefix.

### Centralized Endpoint Configuration

Analytics modules and dashboard endpoints are configured independently from UI components.

### Responsive Healthcare Dashboard

The application adapts to desktop, tablet, and smaller screen sizes.

---

## Technology Stack

| Technology       | Purpose                                    |
| ---------------- | ------------------------------------------ |
| React            | Component-based frontend development       |
| TypeScript       | Static typing and improved maintainability |
| React Router DOM | Client-side routing                        |
| Axios            | REST API communication                     |
| Recharts         | Analytics charts and visualizations        |
| React Markdown   | Markdown response rendering                |
| Lucide React     | UI icons                                   |
| CSS Grid         | Responsive dashboard layouts               |
| FastAPI          | Expected backend analytics API             |

---

## Analytics Modules

HealthSight currently contains nine healthcare analytics modules.

### 1. Cost Analytics

Provides healthcare financial and patient cost analytics.

Supported analytics include:

* Dashboard KPIs
* Average cost
* Median cost
* Total cost
* Cost by age group
* Cost by gender
* Cost by disease
* Cost by Charlson score
* Cost by ICU utilization
* Length-of-stay cost analysis
* High-cost patients
* Cost summary

API prefix:

```text
/cost
```

---

### 2. Disease Analytics

Provides disease prevalence and chronic disease burden analytics.

Supported analytics include:

* Top diseases
* Hypertension
* Type 2 diabetes
* Chronic kidney disease
* Coronary artery disease
* Heart failure
* COPD
* Asthma
* Depression
* Anxiety
* Obesity
* Comorbidity analysis
* Chronic disease burden
* Dashboard KPIs

API prefix:

```text
/disease
```

---

### 3. ICU Analytics

Provides ICU utilization and patient risk analytics.

Supported analytics include:

* Dashboard KPIs
* ICU admission rate
* Average ICU days
* ICU utilization by age group
* ICU utilization by gender
* ICU utilization by Charlson score
* ICU utilization by disease
* High-risk patients
* ICU risk summary

API prefix:

```text
/icu
```

---

### 4. Length of Stay Analytics

Provides hospital length-of-stay analytics.

Supported analytics include:

* Dashboard KPIs
* Average length of stay
* Median length of stay
* LOS by age group
* LOS by gender
* LOS by disease
* LOS by Charlson score
* LOS by ICU utilization
* Long-stay patients
* LOS summary

API prefix:

```text
/los
```

---

### 5. Medication Analytics

Provides medication adherence and medication utilization analytics.

Supported analytics include:

* Dashboard KPIs
* Medication adherence rate
* Medication non-adherence rate
* Top medications
* Adherence by medication
* Adherence by indication
* Generic versus brand analysis
* High-risk patients
* Medication summary

API prefix:

```text
/medication
```

---

### 6. Mortality Analytics

Provides mortality rate and patient risk analytics.

Supported analytics include:

* Dashboard KPIs
* Mortality rate
* Mortality by age group
* Mortality by gender
* Mortality by Charlson score
* Mortality by ICU utilization
* Mortality by disease
* High-risk patients
* Mortality risk summary

API prefix:

```text
/mortality
```

---

### 7. Population Health Analytics

Provides population-level healthcare analytics.

Supported analytics include:

* Population summary
* Age distribution
* Gender distribution
* Smoking analytics
* Alcohol usage
* Exercise analytics
* Obesity analytics
* Hypertension analytics
* Diabetes analytics
* Population risk factors
* Dashboard KPIs

API prefix:

```text
/population
```

This is the default application module.

---

### 8. Readmission Analytics

Provides hospital readmission analytics.

Supported analytics include:

* Dashboard KPIs
* Readmission rate
* Average days to readmission
* Readmission by age group
* Readmission by Charlson score
* Readmission by medication adherence
* High-risk patients
* Readmission risk summary

API prefix:

```text
/readmission
```

---

### 9. Clinical Risk Analytics

Provides clinical risk factor and population risk analytics.

Supported analytics include:

* Dashboard KPIs
* High blood pressure rate
* Obesity rate
* Tachycardia rate
* Abnormal laboratory rate
* Medication non-adherence
* Charlson risk
* High-risk patients
* Risk factor summary
* Population risk score

API prefix:

```text
/risk
```

---

## Project Structure

```text
src/
│
├── api/
│   ├── analyticsApi.ts
│   └── http.ts
│
├── components/
│   ├── ChartView.tsx
│   ├── DashboardView.tsx
│   ├── DataTable.tsx
│   ├── KpiCard.tsx
│   ├── MarkdownCard.tsx
│   ├── ResponseView.tsx
│   └── Sidebar.tsx
│
├── config/
│   ├── dashboardEndpoints.ts
│   └── modules.ts
│
├── pages/
│   └── AnalyticsPage.tsx
│
├── styles/
│   └── global.css
│
├── types/
│   └── analytics.ts
│
├── utils/
│   └── formatters.ts
│
├── App.tsx
└── main.tsx
```

---

## Application Architecture

The application follows a modular frontend architecture.

```text
User
  │
  ▼
React Router
  │
  ▼
AnalyticsPage
  │
  ├── Module Configuration
  │
  ├── Dashboard Endpoint Configuration
  │
  ▼
Analytics API Client
  │
  ▼
Axios HTTP Client
  │
  ▼
FastAPI Backend
  │
  ▼
JSON Response
  │
  ▼
Response Analysis
  │
  ├── KPI Card
  ├── Chart
  ├── Data Table
  └── Markdown Card
```

The architecture separates:

* API communication
* Module configuration
* Dashboard endpoint configuration
* Response transformation
* Visualization
* Formatting
* Routing
* Styling

---

## Dashboard Architecture

Dashboard rendering is handled by:

```text
DashboardView.tsx
```

When the selected endpoint is:

```text
/dashboard-kpis
```

the frontend does not simply call and display the `/dashboard-kpis` FastAPI response.

Instead, `AnalyticsPage` obtains the configured analytics endpoints for the selected module.

Example:

```typescript
cost: [
  "/average-cost",
  "/median-cost",
  "/total-cost",
  "/by-age-group",
  "/by-gender",
  "/by-disease",
  "/by-charlson",
  "/by-icu",
  "/los-analysis",
  "/high-cost-patients",
  "/summary"
]
```

Each endpoint is loaded asynchronously.

```typescript
const results = await Promise.all(
  endpoints.map(async endpoint => {
    try {
      return {
        endpoint,
        data: await fetchEndpoint(`${mod.prefix}${endpoint}`)
      };
    } catch (e: unknown) {
      return {
        endpoint,
        error: apiErrorMessage(e)
      };
    }
  })
);
```

The returned API responses are combined into a React-native analytics dashboard.

---

## API Integration

API communication is separated into two files.

```text
src/api/http.ts
src/api/analyticsApi.ts
```

### Axios HTTP Client

The Axios instance is configured in:

```text
src/api/http.ts
```

The API base URL is obtained from:

```typescript
import.meta.env.VITE_API_BASE_URL
```

Default API URL:

```text
http://127.0.0.1:8000
```

Axios timeout:

```text
120000 milliseconds
```

Equivalent to:

```text
120 seconds
```

Example configuration:

```typescript
export const http = axios.create({
  baseURL: API_BASE_URL,
  timeout: 120000,
});
```

---

## Dashboard KPI Processing

`DashboardView` analyzes each API response.

Primitive values are collected as KPI metrics.

Supported primitive values include:

```text
string
number
boolean
null
```

Example:

```json
{
  "average_cost": 12500,
  "median_cost": 9200,
  "high_cost_rate": 17.5
}
```

The values are converted into:

```text
Average Cost
$12,500.00

Median Cost
$9,200.00

High Cost Rate
17.5%
```

If an API response contains both primitive and complex values, primitive values are rendered as KPIs while complex values continue through the chart and table visualization pipeline.

---

## Dynamic Response Rendering

`ResponseView.tsx` dynamically determines the appropriate presentation based on the API response.

### Null Response

```text
No data returned.
```

### String Response

Rendered using:

```text
MarkdownCard
```

### Array Response

Rendered using:

```text
ChartView
DataTable
```

### Object Response

Primitive fields are rendered as:

```text
KpiCard
```

Complex nested fields are rendered using:

```text
ChartView
DataTable
```

This allows a single reusable response component to display multiple healthcare analytics response formats.

---

## Chart Rendering

Charts are rendered using Recharts.

The main chart component is:

```text
src/components/ChartView.tsx
```

### Automatic Dimension Detection

The chart component analyzes the first data row.

A string field is selected as the category field.

Example:

```text
age_group
disease
gender
medication
name
```

A numeric field is selected as the metric.

Example:

```text
average_cost
patient_count
rate
percentage
score
```

### Pie Chart Selection

When the dataset contains six or fewer records:

```typescript
data.length <= 6
```

the component renders a pie chart.

### Bar Chart Selection

Datasets containing more than six records are displayed as bar charts.

For datasets with more than eight records:

```typescript
data.length > 8
```

a vertical bar chart layout is used.

This improves readability for larger healthcare categories.

### Chart Color Palette

The chart visualization uses the following palette:

```text
#2563eb
#06b6d4
#10b981
#f59e0b
#ef4444
#8b5cf6
#ec4899
#64748b
```

---

## Data Formatting

Formatting utilities are located in:

```text
src/utils/formatters.ts
```

### Title Formatting

API field names are converted into readable labels.

Example:

```text
average_cost
```

becomes:

```text
Average Cost
```

Example:

```text
high-risk-patients
```

becomes:

```text
High Risk Patients
```

### Percentage Formatting

Keys containing:

```text
rate
percent
percentage
```

are displayed as percentages.

Example:

```text
18.456
```

becomes:

```text
18.46%
```

### Currency Formatting

Keys containing:

```text
cost
revenue
amount
```

are formatted as US currency.

Example:

```text
12451697.35
```

becomes:

```text
$12,451,697.35
```

### Boolean Formatting

```text
true  → Yes
false → No
```

### Null Formatting

```text
null → —
```

---

## Routing

Routing is configured using React Router.

Main routes:

```text
/
```

Redirects to the default analytics module.

```text
/analytics/:moduleId
```

Displays the selected healthcare analytics module.

Examples:

```text
/analytics/population
/analytics/cost
/analytics/disease
/analytics/icu
/analytics/los
/analytics/medication
/analytics/mortality
/analytics/readmission
/analytics/risk
```

Unknown routes redirect to:

```text
/
```

---

## Installation

### Prerequisites

Install:

* Node.js 18 or later
* npm
* A running healthcare analytics FastAPI backend

Verify Node.js:

```bash
node --version
```

Verify npm:

```bash
npm --version
```

### Install Dependencies

From the React project root:

```bash
npm install
```

If the project dependencies are not already defined, install the required frontend libraries:

```bash
npm install react react-dom
npm install react-router-dom
npm install axios
npm install recharts
npm install react-markdown
npm install lucide-react
```

Install TypeScript and Vite development dependencies if required:

```bash
npm install -D typescript vite
npm install -D @vitejs/plugin-react
npm install -D @types/react @types/react-dom
```

---

## Environment Configuration

Create a `.env` file in the React project root.

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

If the backend API base URL already contains `/api`:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

The application automatically normalizes a trailing slash.

For example:

```text
http://127.0.0.1:8000/
```

becomes:

```text
http://127.0.0.1:8000
```

---

## Running the Application

### Start the FastAPI Backend

Example:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Start the React Application

```bash
npm run dev
```

The Vite development server normally starts on:

```text
http://localhost:5173
```

Open the application in a web browser.

---

## Backend Requirements

The React frontend expects JSON REST API responses.

### Primitive KPI Response

```json
{
  "average_cost": 12500.75,
  "median_cost": 9250.25,
  "high_cost_rate": 18.5
}
```

### Analytics Array Response

```json
[
  {
    "age_group": "18-30",
    "patient_count": 125
  },
  {
    "age_group": "31-45",
    "patient_count": 245
  },
  {
    "age_group": "46-60",
    "patient_count": 310
  }
]
```

### API Envelope Response

The frontend supports responses wrapped inside a `data` property.

```json
{
  "success": true,
  "data": {
    "average_cost": 12500
  }
}
```

The `unwrap` utility automatically returns:

```json
{
  "average_cost": 12500
}
```

### Markdown Response

An API can return Markdown text.

```text
# Clinical Risk Summary

## High Risk Population

Patients with elevated Charlson scores demonstrate increased ICU utilization.

### Recommendations

- Prioritize high-risk patients
- Improve medication adherence
- Monitor abnormal laboratory results
```

The content is rendered using React Markdown.

---

## API Endpoint Resolution

The application contains API prefix fallback logic.

When the configured API URL is:

```text
http://127.0.0.1:8000
```

and the frontend requests:

```text
/cost/average-cost
```

the application attempts:

```text
/api/cost/average-cost
```

If the server returns HTTP `404`, it retries:

```text
/cost/average-cost
```

Conceptually:

```text
Request
   │
   ▼
/api/cost/average-cost
   │
   ├── Success ──► Return Response
   │
   └── 404
        │
        ▼
/cost/average-cost
        │
        ▼
   Return Response
```

If `VITE_API_BASE_URL` already ends with `/api`, only the clean endpoint path is used.

This allows the React frontend to work with FastAPI applications using different router prefix configurations.

---

## Error Handling

API errors are converted into readable messages using:

```text
apiErrorMessage()
```

The application attempts to display:

* HTTP status
* FastAPI error detail
* Requested API URL

Example:

```text
404 Endpoint not found — http://127.0.0.1:8000/cost/average-cost
```

The UI displays errors using a structured alert panel containing:

```text
Unable to load endpoint
```

and the detailed API error.

Dashboard endpoint failures are isolated.

If one dashboard analytics endpoint fails, other successfully loaded endpoints can still be processed and displayed.

---

## Responsive Design

The application uses CSS Grid and responsive media queries.

### Desktop Layout

```text
Sidebar | Analytics Content
```

The application uses:

```css
grid-template-columns: 270px 1fr;
```

### Dashboard Layout

Dashboard analytics use a two-column grid.

```css
grid-template-columns: repeat(2, minmax(0, 1fr));
```

At screen widths below `1100px`, the dashboard changes to a single-column layout.

### Mobile Layout

Below `900px`:

* Sidebar becomes a horizontal navigation area
* Main application layout becomes single column
* Page header stacks vertically
* Main content padding is reduced

Tables support horizontal scrolling using:

```css
overflow: auto;
```

---

## Adding a New Analytics Module

Open:

```text
src/config/modules.ts
```

Add a new module configuration.

Example:

```typescript
{
  id: "outcomes",
  label: "Outcomes Analytics",
  prefix: "/outcomes",
  endpoints: [
    "/dashboard-kpis",
    "/mortality-rate",
    "/icu-admission-rate",
    "/readmission-rate",
    "/discharge-distribution"
  ]
}
```

The endpoint labels are automatically generated.

For example:

```text
/mortality-rate
```

becomes:

```text
Mortality Rate
```

The module automatically appears in the sidebar because `Sidebar.tsx` renders the configured `modules` array.

---

## Adding Dashboard Endpoints

Open:

```text
src/config/dashboardEndpoints.ts
```

Add dashboard analytics endpoints for the module.

Example:

```typescript
export const dashboardEndpoints: Record<string, string[]> = {
  outcomes: [
    "/mortality-rate",
    "/icu-admission-rate",
    "/readmission-rate",
    "/discharge-distribution"
  ]
};
```

When the user selects:

```text
Dashboard Kpis
```

React loads all configured endpoints and builds the dashboard.

The `/dashboard-kpis` endpoint itself should not be added to `dashboardEndpoints`.

---

## Component Reference

### `Sidebar.tsx`

Responsibilities:

* Display HealthSight branding
* Render analytics modules
* Highlight the active module
* Navigate to analytics routes

---

### `AnalyticsPage.tsx`

Primary analytics page controller.

Responsibilities:

* Read the module ID from the URL
* Resolve module configuration
* Manage endpoint selection
* Load API responses
* Load dashboard endpoint groups
* Manage loading states
* Manage errors
* Select dashboard or response rendering

---

### `DashboardView.tsx`

Builds React-native dashboards from multiple analytics API responses.

Responsibilities:

* Extract KPI metrics
* Separate primitive and complex data
* Generate chart datasets
* Render dashboard sections
* Render detailed tables

---

### `ResponseView.tsx`

Provides generic API response visualization.

Responsibilities:

* Detect response structure
* Render KPI cards
* Render Markdown
* Render charts
* Render tables

---

### `ChartView.tsx`

Provides automatic analytics visualization.

Responsibilities:

* Detect category fields
* Detect numeric fields
* Select pie or bar chart
* Select horizontal or vertical chart orientation
* Apply chart colors

---

### `DataTable.tsx`

Displays structured analytics results.

Responsibilities:

* Detect table columns
* Generate table headers
* Format cell values
* Display nested objects as JSON
* Support horizontal scrolling

---

### `KpiCard.tsx`

Displays individual healthcare KPI metrics.

Each KPI card contains:

* Activity icon
* Formatted KPI title
* Formatted KPI value

---

### `MarkdownCard.tsx`

Displays Markdown analytics summaries using React Markdown.

---

### `analyticsApi.ts`

Provides analytics API requests.

Responsibilities:

* Normalize endpoint paths
* Handle `/api` prefix fallback
* Execute HTTP GET requests
* Return JSON API responses

---

### `http.ts`

Provides centralized Axios configuration.

Responsibilities:

* Configure the backend base URL
* Configure API timeout
* Provide Axios HTTP client
* Normalize API errors

---

### `modules.ts`

Central registry for healthcare analytics modules and endpoints.

---

### `dashboardEndpoints.ts`

Defines the analytics endpoints used to compose React-native dashboards.

---

### `formatters.ts`

Provides reusable formatting utilities.

Functions include:

```text
titleCase()
fmt()
isPrimitive()
numericEntries()
unwrap()
```

---

## Design Principles

The HealthSight frontend follows several architectural principles.

### Configuration Over Duplication

Healthcare modules are defined using configuration rather than separate pages for every analytics domain.

### Reusable Visualization Components

The same chart, KPI, table, and Markdown components are shared across analytics modules.

### API Response Intelligence

The frontend analyzes JSON response structures before selecting a visual representation.

### Separation of Concerns

API communication, configuration, formatting, rendering, routing, and styling are maintained in separate modules.

### Dashboard Composition

Dashboards are composed from multiple focused analytics APIs instead of depending entirely on a backend-rendered dashboard response.

### Graceful API Compatibility

The `/api` prefix fallback improves compatibility with different FastAPI router configurations.

---

## Future Enhancements

Potential enhancements include:

* Line charts for time-series analytics
* Area charts for patient volume trends
* Scatter plots for correlation analytics
* Radar charts for clinical risk profiles
* Heatmaps for disease comorbidity analysis
* Chart legends and custom tooltips
* Chart export to PNG
* Dashboard export to PDF
* CSV and Excel downloads
* Date-range filtering
* Gender filters
* Age-group filters
* Disease filters
* Charlson risk filters
* Global dashboard filters
* React Query for API caching
* API request cancellation
* Skeleton loaders
* Lazy-loaded analytics modules
* Dark mode
* Role-based access control
* Authentication and authorization
* Audit logging
* Unit testing with Vitest
* Component testing with React Testing Library
* End-to-end testing with Playwright
* Docker deployment
* Kubernetes deployment
* Azure deployment
* CI/CD automation

---

## Recommended Production Architecture

```text
Browser
   │
   ▼
React + TypeScript
   │
   ├── React Router
   ├── Analytics Components
   ├── Recharts
   └── Axios
         │
         ▼
     API Gateway
         │
         ▼
      FastAPI
         │
   ┌─────┼──────────┐
   │     │          │
   ▼     ▼          ▼
Analytics Service  ML Service
   │                  │
   ▼                  ▼
PostgreSQL        MLflow Models
   │
   ▼
Healthcare Data Platform
```

---

## Summary

HealthSight provides a reusable React and TypeScript architecture for building healthcare analytics dashboards on top of FastAPI analytics services.

The application currently supports:

* Cost Analytics
* Disease Analytics
* ICU Analytics
* Length of Stay Analytics
* Medication Analytics
* Mortality Analytics
* Population Health Analytics
* Readmission Analytics
* Clinical Risk Analytics

Its configuration-driven design enables new healthcare analytics modules and REST endpoints to be integrated with minimal frontend changes.

Dynamic KPI extraction, automatic chart selection, responsive tables, Markdown summaries, centralized API handling, and React-native dashboard composition provide a flexible foundation for enterprise healthcare intelligence applications.

---

## Application Name

**HealthSight**

### Healthcare Analytics Platform

Built with React, TypeScript, Axios, React Router, Recharts, and FastAPI.
