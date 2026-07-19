import streamlit as st

from api.client import get_data
from components.response_view import render_error, render_metric_cards, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="Mortality", page_icon="📉", layout="wide")
render_sidebar()
st.title("📉 Mortality Analytics")

rate = get_data("/mortality/rate")
if not render_error(rate):
    render_metric_cards(rate.get("data", {}), columns=1)

st.divider()
st.subheader("High Risk Patients")
risk = get_data("/mortality/high-risk-patients")
if not render_error(risk):
    render_table(risk.get("data"))
