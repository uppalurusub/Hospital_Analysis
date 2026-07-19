import streamlit as st

from api.client import BASE_URL


def render_sidebar() -> None:
    """Render shared application navigation/help information."""
    with st.sidebar:
        st.title("Healthcare Analytics")
        st.caption("Enterprise analytics dashboard")
        st.divider()
        st.markdown("**API Base URL**")
        st.code(BASE_URL, language=None)
        st.info("Use the Streamlit page navigation to open an analytics module.")
