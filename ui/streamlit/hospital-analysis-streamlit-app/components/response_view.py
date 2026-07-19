from typing import Any

import pandas as pd
import streamlit as st

from utils.formatters import format_metric, humanize_label


def render_error(response: dict[str, Any]) -> bool:
    """Return True when an API response contains an error."""
    if not response.get("success", True):
        st.error(response.get("error", "Unable to load data."))
        return True
    return False


def render_metric_cards(data: dict[str, Any], columns: int = 4) -> None:
    """Render scalar dictionary values as responsive metric cards."""
    items = list(data.items())
    if not items:
        st.info("No metrics available.")
        return

    for start in range(0, len(items), columns):
        row = items[start : start + columns]
        cols = st.columns(len(row))
        for col, (key, value) in zip(cols, row):
            col.metric(humanize_label(key), format_metric(value, key))


def render_dashboard_sections(data: dict[str, Any]) -> None:
    """Render nested API dashboard responses using cards and tables."""
    for title, value in data.items():
        st.subheader(humanize_label(title))

        if isinstance(value, dict):
            render_metric_cards(value)
        elif isinstance(value, list):
            if value and isinstance(value[0], dict):
                st.dataframe(pd.DataFrame(value), use_container_width=True, hide_index=True)
            else:
                st.write(value)
        else:
            st.metric(humanize_label(title), format_metric(value, title))


def render_table(data: Any, empty_message: str = "No records available.") -> None:
    if data is None or data == []:
        st.info(empty_message)
        return
    st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
