import streamlit as st

from components.sidebar import render_sidebar

st.set_page_config(
    page_title="Healthcare Analytics Platform",
    page_icon="🏥",
    layout="wide",
)

render_sidebar()

st.title("🏥 Healthcare Analytics Platform")
st.markdown(
    """
    Welcome to the **Enterprise Healthcare Analytics Dashboard**.

    ### Modules Available
    - Population Health
    - Disease Analytics
    - Clinical Risk Analytics
    - Readmission Analytics
    - Mortality Analytics
    - ICU Analytics
    - Length of Stay Analytics
    - Cost Analytics
    - Medication Analytics

    Select a page from the navigation panel to explore KPIs and patient-level analytics.
    """
)
