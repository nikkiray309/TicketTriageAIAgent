import requests
import streamlit as st

# -----------------------------
# Configuration
# -----------------------------

API_URL = "http://127.0.0.1:8000/api/v1/analyze"

SEVERITY_CONFIG = {
    "low": ("🟢", "Low"),
    "medium": ("🟡", "Medium"),
    "high": ("🟠", "High"),
    "critical": ("🔴", "Critical"),
}

# -----------------------------
# Page
# -----------------------------

st.set_page_config(
    page_title="Support Ticket Triage Agent",
    page_icon="🎫",
    layout="wide",
)

st.title("🎫 Support Ticket Triage Agent")

st.caption(
    "AI-assisted support ticket analysis powered by FastAPI + LLM Agent"
)

st.divider()

# -----------------------------
# Ticket Input
# -----------------------------

ticket = st.text_area(
    "Customer Ticket",
    height=220,
    placeholder="Paste customer support ticket here..."
)

# -----------------------------
# Analyze Button
# -----------------------------

if st.button("Analyze Ticket", use_container_width=True):

    if not ticket.strip():

        st.warning("Please enter a support ticket.")

    else:

        with st.spinner("Analyzing ticket..."):

            response = requests.post(
                API_URL,
                json={
                    "ticket": ticket
                }
            )

        if response.status_code != 200:
            st.error("Backend returned an error.")
            st.write(response.text)
            st.stop()

        result = response.json()
        data = result["data"]

        st.divider()

        # ==========================================
        # Summary
        # ==========================================

        st.subheader("Summary")
        st.write(data["summary"])

        # ==========================================
        # Issue Type + Severity
        # ==========================================

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Issue Type")
            st.info(data["issue_type"])

        with col2:

            st.subheader("Severity")

            severity = data["severity"].lower()

            icon, label = SEVERITY_CONFIG.get(
                severity,
                ("⚪", severity.title())
            )

            st.markdown(f"# {icon} {label}")

        # ==========================================
        # Recommendations
        # ==========================================

        st.divider()

        st.subheader("Recommended Next Steps")
        st.text(data["recommended_next_steps"])

        # for step in data["recommended_next_steps"]:

        #     st.checkbox(
        #         step,
        #         disabled=True
        #     )

        # ==========================================
        # Escalation
        # ==========================================

        st.divider()

        st.subheader("Escalation")

        if data["needs_escalation"]:

            st.error(data["reason_for_escalation"])

        else:

            st.success("No escalation required.")

        # ==========================================
        # Customer Response
        # ==========================================

        st.divider()

        st.subheader("Customer Response Draft")

        st.text_area(
        "Customer Response Draft",
        value=data["customer_response_draft"],
        height=220
        )
        
        # ==========================================
        # Validation
        # ==========================================

        st.divider()

        st.subheader("Validation")

        validation = data["validation"]

        if validation["passed"]:

            st.success("Validation Passed")

        else:

            st.error("Validation Failed")

        issues = validation.get("issues", [])

        if issues:

            st.markdown("### Validation Issues")

            for issue in issues:

                st.warning(issue)