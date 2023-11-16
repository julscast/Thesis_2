import streamlit as st


st.set_page_config(page_title="Sentiment Analysis of Halalan 2022 Twitter Data", page_icon="🗳️", 
                   layout="wide", initial_sidebar_state="expanded")

st.title("Sentiment Analysis of Halalan 2022 Twitter Data")
st.sidebar.success("Select a page above.")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

