import streamlit as st

def render_validation(validation):
    st.subheader("Validation")
    if validation["passed"]:
        st.success("Validation Passed")
    else:
        st.error("Validation Failed")

    issues = validation.get("issues", [])
    if issues:
        st.markdown("### Issues")
        for issue in issues:
            st.warning(issue)