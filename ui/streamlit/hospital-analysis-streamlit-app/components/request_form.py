from collections.abc import Callable

import streamlit as st


def render_refresh_button(
    label: str = "Refresh data",
    key: str = "refresh_data",
    on_click: Callable[[], None] | None = None,
) -> bool:
    """Render a reusable refresh/request action."""
    return st.button(
        label,
        key=key,
        type="primary",
        use_container_width=True,
        on_click=on_click,
    )
