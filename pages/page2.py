import streamlit  as st
import database
import reasoning
import stats
import matplotlib.pyplot as plt
import pandas as pd
import io


page2_bg_design = """
<style>
[data-testid="stApp"]{

}
</style>
"""

def convert_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

db_path = 'feedback2.db'
df = database.get_reasons()
buffer = io.BytesIO()

st.set_page_config(
    page_title="FYP Project",
    page_icon="",
)
st.markdown(page2_bg_design, unsafe_allow_html=True)
st.title("Statistics & Summary")
st.subheader("Final Year Project - CS3072")
st.text("View all reasons, Summarize and view statistics on feedback entered so far")
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
    file_name='large_df.csv',
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