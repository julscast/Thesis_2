import streamlit as st
from stat_1 import stats
from topic import topics


st.set_page_config(page_title="Sentiment Analysis of Halalan 2022 Twitter Data", page_icon="🗳️", 
                    layout="wide")

def start_main():

    st.title("Sentiment Analysis of Halalan 2022 Twitter Data")

    selected_tab = st.sidebar.selectbox("Navigation", ["Statistics", "Topic Models", "Sentiment Analysis"])

    if selected_tab == "Statistics":
        stats()
    elif selected_tab == "Topic Models":
        st.write("Topic Models")
        topics()
    elif selected_tab == "Sentiment Analysis":
        st.write("Sentiment Analysis")

def main():
    start_main()

if __name__ == "__main__":
    main()