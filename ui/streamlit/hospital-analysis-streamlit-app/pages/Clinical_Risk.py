import streamlit as st

from api.client import get_data
from components.response_view import render_dashboard_sections, render_error, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="Clinical Risk", page_icon="⚠️", layout="wide")
render_sidebar()
st.title("⚠️ Clinical Risk Analytics")

kpis = get_data("/risk/dashboard-kpis")
if not render_error(kpis):
    render_dashboard_sections(kpis.get("data", {}))

st.divider()
st.subheader("High Risk Patients")
high_risk = get_data("/risk/high-risk-patients")
if not render_error(high_risk):
    render_table(high_risk.get("data"))
