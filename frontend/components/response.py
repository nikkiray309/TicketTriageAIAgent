import streamlit as st


def render_customer_response(response):
    st.subheader("Customer Response Draft")
    st.text_area(
        "",
        value=response,
        height=220
    )