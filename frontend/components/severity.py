import streamlit as st
from frontend.utils import SEVERITY_CONFIG

def render_severity(severity: str):
    severity = severity.lower()
    config = SEVERITY_CONFIG.get(
        severity,
        {
            "icon": "⚪",
            "label": severity.title()
        }
    )

    st.subheader("Severity")
    st.markdown(
        f"## {config['icon']} {config['label']}"
    )