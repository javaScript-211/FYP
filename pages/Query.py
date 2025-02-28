import streamlit  as st
import reasoning
import database
import io

page3_bg_design = """
<style>
[data-testid="stHeader"]{
    background-color: #E55451;
}
</style>
"""
session = [[]]
buffer = io.BytesIO()

st.set_page_config(page_title="FYP Project",page_icon="",layout="wide")

def convert_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

st.title("Queries/Discussions")
st.divider()
st.write("This section is dedicated for questions about the feedback to be answered through the AI solution")
st.markdown(page3_bg_design, unsafe_allow_html=True)

feedback = st.text_area("Enter your query here :")
submission = st.button("Submit", type="primary", )

if submission:
    result = reasoning.claudeAPI("query","-", feedback)
    st.subheader("Response to query") 
    st.write(result)
    
    database.enter_query(feedback, result)
    df = database.get_queries()
    st.dataframe(df)
    
    st.divider()
    st.subheader("Option to Download") 
    csv = convert_to_csv(df)
    downloadbtn = st.download_button(label="Download Reasons",
    data=csv,
    file_name='Feedback_queries.csv',
    mime='text/csv'
    )
