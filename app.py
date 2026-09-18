import streamlit as st
import streamlit.components.v1 as components

st.title("Mon dashboard Power BI du crédit breton")

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=6bb0bcd0-418c-4024-9f37-7cf6cafa830c&autoAuth=true&ctid=9a50b308-0f88-47aa-b736-35f811873955"

components.iframe(
    powerbi_url,
    height=700,
    scrolling=True
)
