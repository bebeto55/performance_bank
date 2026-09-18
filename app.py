import streamlit as st
import streamlit.components.v1 as components

import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration en mode wide
st.set_page_config(layout="wide")

# 2. Supression des marges latérales de Streamlit via du CSS
st.markdown(
    """
    <style>
        /* Supprime les marges à gauche et à droite */
        .appview-container .main .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        /* Force l'élément iframe à prendre tout l'espace disponible */
        iframe {
            width: 100% !important;
        }
    </style>
""",
    unsafe_allow_html=True,
)
st.title("Mon dashboard du crédit breton")

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=6bb0bcd0-418c-4024-9f37-7cf6cafa830c&autoAuth=true&ctid=9a50b308-0f88-47aa-b736-35f811873955"



components.iframe(
    powerbi_url,
    height=1300,
    width=None,
    scrolling=True
)
