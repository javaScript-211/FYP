import streamlit  as st
import multiEmoteFT
import database
import reasoning



page_bg_design = """
<style>
[data-testid="stHeader"]{
    background-color: #E55451;
}

[data-testid="stHorizontalBlock"]{
    background-color: #F5F5F5;
    padding-left: 25px;
    padding-right: 25px;
    padding-bottom: 20px;
    padding-top: 20px;
[data-testid="stTextAreaRootElement"]{
    background-color: #A9A9A9;
}
</style>
"""

emotionDetector = multiEmoteFT.EmotionDetector2()
st.session_state.count = 0
@st.cache_resource
def display_emotions(text:str, top_n, count):
    st.session_state.count += 1
    emotion1, emotion2, emotion3 = emotionDetector.detect_emotion(text, top_n)
    reasons = reasoning.claudeAPI("reason", emotion1[0], feedback)
    database.enter_data(feedback, option, emotion1[0], emotion2[0], emotion3[0], reasons)
    st.write(emotion1)
    st.empty()
    st.write(emotion2)
    st.empty()
    st.write(emotion3)
    st.empty()
    "### Reasons for emotions"
    st.empty()
    st.write(reasons)
    return count

st.set_page_config(
    page_title="FYP Project",
    page_icon="",
    layout="wide"
)

st.markdown(page_bg_design, unsafe_allow_html=True)
st.title("Sentiment Analysis of Feedback")
st.divider()
st.subheader("Final Year Project - CS3072")
st.text("This solution was designed as a way that allows feedback to be entered and processed\nin one tool. Teachers or students can enter feedback and AI will find emotions and \nkey reasons.")

st.sidebar.header("Navigation")

st.divider()
st.empty()
col1_1, col2_1 = st.columns(2)
with col1_1:
    option = st.selectbox(
        "Select a module:",
        ("CS2001","CS2002","CS2003","CS2004","CS2005"),
    )
with col2_1:
    st.text("More modules & options coming\nsoon...")
st.divider()
st.empty()
st.empty()
col1, col2 = st.columns(2)
with col1:
    "### Feedback Input"
    st.empty()
    st.empty()
    feedback = st.text_area("Enter your feedback here for "+option+":")
    submission = st.button("Submit", type="primary", )
    st.text("""Any information entered into the system will be stored anonymously into a 
database. Furthermore, academic staff and personnel will be able to read 
and process.""")
with col2:
    "### Emotion Results"
    st.empty()
    if submission:
        st.toast('Feedback has been submitted')
        st.session_state.count += 1
        display_emotions(feedback, 3, st.session_state.count)
    
    st.write('Number of feedback', st.session_state.count)