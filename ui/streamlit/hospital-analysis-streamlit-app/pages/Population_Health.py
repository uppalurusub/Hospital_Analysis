import streamlit as st

from api.client import get_data
from components.response_view import render_error, render_metric_cards, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="Population Health", page_icon="👥", layout="wide")
render_sidebar()
st.title("👥 Population Health Analytics")

summary = get_data("/population/summary")
if not render_error(summary):
    data = summary.get("data", {})
    total = data.get("total_patients", 0)
    metrics = {
        "total_patients": total,
        "average_age": data.get("average_age"),
        "male_pct": (data.get("male_patients", 0) / total * 100) if total else 0,
        "female_pct": (data.get("female_patients", 0) / total * 100) if total else 0,
        "average_bmi": data.get("average_bmi"),
    }
    render_metric_cards(metrics, columns=5)

st.divider()
st.subheader("Age Distribution")
age = get_data("/population/age-distribution")
if not render_error(age):
    render_table(age.get("data"))
