import streamlit  as st
import database
import reasoning
import stats
import matplotlib.pyplot as plt
import pandas as pd
import io
import pathlib

st.set_page_config(
    page_title="FYP Project",
    page_icon="",
    layout="wide"
)

page2_bg_design = """
<style>
[data-testid="stHeader"]{
    background-color: #E55451;
}
</style>
"""

def convert_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

db_path = 'feedback2.db'
df = database.get_reasons()
buffer = io.BytesIO()

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}<\style")

css_path = pathlib.Path(r"\Users\James\Documents\CS-3Yr\project\sentanalysis2\styles.css")
load_css(css_path)

st.markdown(page2_bg_design, unsafe_allow_html=True)
st.title("Statistics & Summary")
st.divider()
st.subheader( "What is this page for?")
st.write("""View all reasons stored so far and a summary of reviews for each module.\n 
View statistics on the feedback entered the system""")
st.divider()
emotion = ""
feedback = ""

col1, col2,col3 = st.columns(3)
with col1:
    Databtn = st.button("View Reasons", type="primary")
with col2:
    Summarybtn = st.button("View Summary", type="primary")
    
with col3:
    Graphbtn = st.button("View Statistics", type="primary")

csv = convert_to_csv(df)

download1 = st.download_button(
    label="Download Reasons",
    data=csv,
    file_name='Feedback_reasons.csv',
    mime='text/csv'
)

if Summarybtn:
    textType = "summary"
    result = reasoning.claudeAPI(textType, emotion, feedback)
    summaryData = result
    st.write(result)

if Databtn:
    st.dataframe(df, hide_index=True)

elif Graphbtn:
    modules, counts = stats.graphPC()

    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=modules,autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    emotions, counts3 = stats.emotionCount()
    fig3, ax3 = plt.subplots()
    ax3.pie(counts3, labels=emotions,autopct='%1.1f%%', startangle=90,)
    ax3.axis('equal')
    st.pyplot(fig3)

    dates, counts2 = stats.graphLine()
    
    df = pd.DataFrame({'Date':pd.to_datetime(dates, format='%d/%m/%Y'), 'Value':counts2})
    df['Cumulative'] = df['Value'].cumsum()
    fig2, ax2 = plt.subplots()
    ax2.plot(df['Date'], df['Cumulative'], marker='o', linestyle='-')
    ax2.set_title("Feedback entered on the system")
    ax2.grid(True)
    ax2.set_xticks(df['Date'])
    st.pyplot(fig2)