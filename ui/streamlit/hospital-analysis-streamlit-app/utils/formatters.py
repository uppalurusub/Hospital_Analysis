from typing import Any


def humanize_label(value: str) -> str:
    return value.replace("_", " ").strip().title()


def format_metric(value: Any, key: str = "") -> str:
    if value is None:
        return "N/A"
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if isinstance(value, (int, float)):
        key_lower = key.lower()
        if "pct" in key_lower or "percent" in key_lower or "rate" in key_lower:
            return f"{value:,.2f}%"
        if "usd" in key_lower or "cost" in key_lower or "revenue" in key_lower:
            return f"${value:,.2f}"
        if isinstance(value, float):
            return f"{value:,.2f}"
        return f"{value:,}"
    return str(value)
