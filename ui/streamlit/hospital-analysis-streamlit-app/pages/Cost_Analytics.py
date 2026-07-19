import streamlit as st

from api.client import get_data
from components.response_view import render_error, render_metric_cards, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="Cost Analytics", page_icon="💰", layout="wide")
render_sidebar()
st.title("💰 Cost Analytics")

average = get_data("/cost/average-cost")
total = get_data("/cost/total-cost")
metrics = {}
if not render_error(average):
    metrics["average_cost_per_admission_usd"] = average.get("data", {}).get("average_cost_per_admission_usd")
if not render_error(total):
    metrics["total_hospital_cost_usd"] = total.get("data", {}).get("total_hospital_cost_usd")
if metrics:
    render_metric_cards(metrics, columns=2)

st.divider()
st.subheader("High Cost Patients")
patients = get_data("/cost/high-cost-patients")
if not render_error(patients):
    render_table(patients.get("data"))
