import streamlit as st

from api.client import get_data
from components.response_view import render_error, render_metric_cards, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="Length of Stay", page_icon="🛏️", layout="wide")
render_sidebar()
st.title("🛏️ Length of Stay Analytics")

average = get_data("/los/average-los")
median = get_data("/los/median-los")
metrics = {}
if not render_error(average):
    metrics["average_los_days"] = average.get("data", {}).get("average_los_days")
if not render_error(median):
    metrics["median_los_days"] = median.get("data", {}).get("median_los_days")
if metrics:
    render_metric_cards(metrics, columns=2)

st.divider()
st.subheader("Long Stay Patients")
patients = get_data("/los/long-stay-patients")
if not render_error(patients):
    render_table(patients.get("data"))
