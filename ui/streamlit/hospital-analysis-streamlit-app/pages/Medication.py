import streamlit as st

from api.client import get_data
from components.response_view import render_error, render_metric_cards, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="Medication Analytics", page_icon="💊", layout="wide")
render_sidebar()
st.title("💊 Medication Analytics")

adherence = get_data("/medication/adherence-rate")
non_adherence = get_data("/medication/non-adherence-rate")
metrics = {}
if not render_error(adherence):
    metrics["overall_adherence_pct"] = adherence.get("data", {}).get("overall_adherence_pct")
if not render_error(non_adherence):
    metrics["non_adherence_rate_pct"] = non_adherence.get("data", {}).get("non_adherence_rate_pct")
if metrics:
    render_metric_cards(metrics, columns=2)

st.divider()
st.subheader("Top Medications")
top_medications = get_data("/medication/top-medications")
if not render_error(top_medications):
    render_table(top_medications.get("data"))

st.divider()
st.subheader("High Risk Patients")
patients = get_data("/medication/high-risk-patients")
if not render_error(patients):
    render_table(patients.get("data"))
