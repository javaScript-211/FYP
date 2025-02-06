import streamlit  as st
import reasoning

page3_bg_design = """
<style>

"""

st.title("Queries")
st.text("This section is dedicated for questions about the feedback to\n be answered through the AI solution")
st.markdown(page3_bg_design, unsafe_allow_html=True)

feedback = st.text_area("Enter your query here :")
submission = st.button("Submit", type="primary", )

if submission:
    result = reasoning.claudeAPI("query","", feedback)
    st.write("Response to query")
    st.write(result)