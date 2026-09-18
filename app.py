import streamlit as st
import streamlit.components.v1 as components

st.title("Mon dashboard Power BI du crédit breton")

powerbi_url = "https://app.powerbi.com/links/Nf5ZtJJ1Mx?ctid=9a50b308-0f88-47aa-b736-35f811873955&pbi_source=linkShare"

components.iframe(
    powerbi_url,
    height=700,
    scrolling=True
)
