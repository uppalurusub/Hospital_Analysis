import streamlit as st

from api.client import get_data
from components.response_view import render_error, render_metric_cards, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="ICU Analytics", page_icon="🏥", layout="wide")
render_sidebar()
st.title("🏥 ICU Analytics")

rate = get_data("/icu/admission-rate")
days = get_data("/icu/average-days")
metrics = {}
if not render_error(rate):
    metrics["icu_admission_rate_pct"] = rate.get("data", {}).get("icu_admission_rate_pct")
if not render_error(days):
    metrics["average_icu_days"] = days.get("data", {}).get("average_icu_days")
if metrics:
    render_metric_cards(metrics, columns=2)

st.divider()
st.subheader("ICU High Risk Patients")
patients = get_data("/icu/high-risk-patients")
if not render_error(patients):
    render_table(patients.get("data"))
