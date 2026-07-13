import streamlit as st

def render_recommendations(steps):
    st.subheader("Recommended Next Steps")
    for step in steps:
        st.checkbox(
            step,
            value=False,
            disabled=True
        )