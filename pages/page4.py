import streamlit  as st
import reasoning
import pandas as pd
import database
import io

st.set_page_config(
    page_title="FYP Project",
    page_icon="",
    layout="wide"
)

st.title("Judge LLM")
st.divider()
st.text("""This section is dedicated to comparing different models and how they judge the feedback from the system. Comparing the results
and if they are similar to the human counterparts in this particular task""")