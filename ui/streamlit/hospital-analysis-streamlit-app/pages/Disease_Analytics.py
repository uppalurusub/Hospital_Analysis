import streamlit as st

from api.client import get_data
from components.response_view import render_error, render_metric_cards, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="Disease Analytics", page_icon="🩺", layout="wide")
render_sidebar()
st.title("🩺 Disease Analytics")

responses = {
    "hypertension_pct": get_data("/disease/hypertension"),
    "diabetes_pct": get_data("/disease/type2-diabetes"),
    "ckd_pct": get_data("/disease/chronic-kidney-disease"),
}
metrics = {}
for key, response in responses.items():
    if not render_error(response):
        metrics[key] = response.get("data", {}).get("prevalence_pct")
if metrics:
    render_metric_cards(metrics, columns=3)

st.divider()
st.subheader("Disease Distribution")
diseases = get_data("/disease/top-diseases")
if not render_error(diseases):
    render_table(diseases.get("data"))
