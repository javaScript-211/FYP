import streamlit  as st
import reasoning
import pandas as pd
import database
import io

page4_bg_design = """
<style>
[data-testid="stHeader"]{
    background-color: #E55451;
}
</style>
"""
st.markdown(page4_bg_design, unsafe_allow_html=True)
st.set_page_config(
    page_title="FYP Project",
    page_icon="",
    layout="wide"
)

st.title("Judge LLM")
st.divider()
st.text("""This section is dedicated to comparing different models and how they judge the feedback from the system. Comparing the results
and if they are similar to the human counterparts in this particular task""")