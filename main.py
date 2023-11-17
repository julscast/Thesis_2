import streamlit as st
from stat_1 import stats
from topic import topics
from sentiment import sentiment

st.set_page_config(page_title="Analysis of Halalan 2022 Twitter Data", page_icon="🗳️", 
                    layout="wide", initial_sidebar_state="expanded")

def start_main():

    st.title("Analysis of Halalan 2022 Twitter Data 🗳️")

    selected_tab = st.sidebar.selectbox("Navigation", ["Statistics", "Topic Models", "Sentiment Analysis"])

    if selected_tab == "Statistics":
        stats()
    elif selected_tab == "Topic Models":
        st.write("Topic Models")
        topics()
    elif selected_tab == "Sentiment Analysis":
        sentiment()

def main():
    start_main()

if __name__ == "__main__":
    main()