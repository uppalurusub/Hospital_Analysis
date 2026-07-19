export const dashboardEndpoints: Record<string, string[]> = {
  cost: ["/average-cost", "/median-cost", "/total-cost", "/by-age-group", "/by-gender", "/by-disease", "/by-charlson", "/by-icu", "/los-analysis", "/high-cost-patients", "/summary"],
  icu: ["/admission-rate", "/average-days", "/by-age-group", "/by-gender", "/by-charlson", "/by-disease", "/high-risk-patients", "/risk-summary"],
  los: ["/average-los", "/median-los", "/by-age-group", "/by-gender", "/by-disease", "/by-charlson", "/by-icu", "/long-stay-patients", "/summary"],
  medication: ["/adherence-rate", "/non-adherence-rate", "/top-medications", "/adherence-by-medication", "/adherence-by-indication", "/generic-vs-brand", "/high-risk-patients", "/summary"],
  mortality: ["/rate", "/by-age-group", "/by-gender", "/by-charlson", "/by-icu", "/by-disease", "/high-risk-patients", "/risk-summary"],
  readmission: ["/rate", "/average-days", "/by-age-group", "/by-charlson", "/by-adherence", "/high-risk-patients", "/risk-summary"],
  risk: ["/high-bp-rate", "/obesity-rate", "/tachycardia-rate", "/abnormal-lab-rate", "/medication-non-adherence", "/charlson-risk", "/high-risk-patients", "/risk-factor-summary", "/population-risk-score"],
  population: ["/summary", "/age-distribution", "/gender-distribution", "/smoking", "/alcohol", "/exercise", "/obesity", "/hypertension", "/diabetes", "/risk-factors"],
  disease: ["/top-diseases", "/hypertension", "/type2-diabetes", "/chronic-kidney-disease", "/coronary-artery-disease", "/heart-failure", "/copd", "/asthma", "/depression", "/anxiety", "/obesity", "/comorbidity-analysis", "/chronic-disease-burden"]
};
