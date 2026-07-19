import streamlit as st

from api.client import get_data
from components.response_view import render_dashboard_sections, render_error, render_table
from components.sidebar import render_sidebar

st.set_page_config(page_title="Readmission", page_icon="🔁", layout="wide")
render_sidebar()
st.title("🔁 Readmission Analytics")

kpis = get_data("/readmission/dashboard-kpis")
if not render_error(kpis):
    render_dashboard_sections(kpis.get("data", {}))

st.divider()
st.subheader("High Risk Patients")
patients = get_data("/readmission/high-risk-patients")
if not render_error(patients):
    render_table(patients.get("data"))
