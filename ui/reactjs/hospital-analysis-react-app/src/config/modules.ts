import type { ModuleConfig } from "../types/analytics";
const raw = [
  {
    "id": "cost",
    "label": "Cost Analytics",
    "prefix": "/cost",
    "endpoints": [
      "/dashboard-kpis",
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
  },
  {
    "id": "disease",
    "label": "Disease Analytics",
    "prefix": "/disease",
    "endpoints": [
      "/top-diseases",
      "/hypertension",
      "/type2-diabetes",
      "/chronic-kidney-disease",
      "/coronary-artery-disease",
      "/heart-failure",
      "/copd",
      "/asthma",
      "/depression",
      "/anxiety",
      "/obesity",
      "/comorbidity-analysis",
      "/chronic-disease-burden",
      "/dashboard-kpis"
    ]
  },
  
  
  
  {
    "id": "icu",
    "label": "ICU Analytics",
    "prefix": "/icu",
    "endpoints": [
      "/dashboard-kpis",
      "/admission-rate",
      "/average-days",
      "/by-age-group",
      "/by-gender",
      "/by-charlson",
      "/by-disease",
      "/high-risk-patients",
      "/risk-summary"
    ]
  },
  {
    "id": "los",
    "label": "Length of Stay Analytics",
    "prefix": "/los",
    "endpoints": [
      "/dashboard-kpis",
      "/average-los",
      "/median-los",
      "/by-age-group",
      "/by-gender",
      "/by-disease",
      "/by-charlson",
      "/by-icu",
      "/long-stay-patients",
      "/summary"
    ]
  },
  {
    "id": "medication",
    "label": "Medication Analytics",
    "prefix": "/medication",
    "endpoints": [
      "/dashboard-kpis",
      "/adherence-rate",
      "/non-adherence-rate",
      "/top-medications",
      "/adherence-by-medication",
      "/adherence-by-indication",
      "/generic-vs-brand",
      "/high-risk-patients",
      "/summary"
    ]
  },
  {
    "id": "mortality",
    "label": "Mortality Analytics",
    "prefix": "/mortality",
    "endpoints": [
      "/dashboard-kpis",
      "/rate",
      "/by-age-group",
      "/by-gender",
      "/by-charlson",
      "/by-icu",
      "/by-disease",
      "/high-risk-patients",
      "/risk-summary"
    ]
  },
  
  {
    "id": "population",
    "label": "Population Health Analytics",
    "prefix": "/population",
    "endpoints": [
      "/summary",
      "/age-distribution",
      "/gender-distribution",
      "/smoking",
      "/alcohol",
      "/exercise",
      "/obesity",
      "/hypertension",
      "/diabetes",
      "/risk-factors",
      "/dashboard-kpis"
    ]
  },
  
  {
    "id": "readmission",
    "label": "Readmission Analytics",
    "prefix": "/readmission",
    "endpoints": [
      "/dashboard-kpis",
      "/rate",
      "/average-days",
      "/by-age-group",
      "/by-charlson",
      "/by-adherence",
      "/high-risk-patients",
      "/risk-summary"
    ]
  },
  {
    "id": "risk",
    "label": "Clinical Risk Analytics",
    "prefix": "/risk",
    "endpoints": [
      "/dashboard-kpis",
      "/high-bp-rate",
      "/obesity-rate",
      "/tachycardia-rate",
      "/abnormal-lab-rate",
      "/medication-non-adherence",
      "/charlson-risk",
      "/high-risk-patients",
      "/risk-factor-summary",
      "/population-risk-score"
    ]
  }
];
const title = (s:string) => s.replace(/^\//,"").replace(/-/g," ").replace(/\b\w/g,c=>c.toUpperCase());
export const modules: ModuleConfig[] = raw.map(m => ({...m, endpoints:m.endpoints.map((path:string)=>({path,label:title(path)}))}));
export const defaultModule = modules.find(m=>m.id==="population") ?? modules[0];
