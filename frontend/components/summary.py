import streamlit as st

def render_summary(summary, issue_type):
    st.subheader("Summary")
    st.write(summary)
    st.subheader("Issue Type")
    st.info(issue_type)