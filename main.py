import streamlit as st
from stat_1 import stats 

def main():
    st.set_page_config(page_title="Sentiment Analysis of Halalan 2022 Twitter Data", page_icon="🗳️", 
                    layout="wide")

    st.title("Sentiment Analysis of Halalan 2022 Twitter Data")

    selected_tab = st.sidebar.selectbox("Navigation", ["Statistics", "Topic Models", "Sentiment Analysis"])

    if selected_tab == "Statistics":
        stats()
    elif selected_tab == "Topic Models":
        st.write("Topic Modeling")
    elif selected_tab == "Sentiment Analysis":
        st.write("Sentiment Analysis")

if __name__ == "__main__":
    main()