import streamlit as st
import pandas as pd
import numpy as np

def sentiment():
    dataset_options = ["Pre-Election", "During Election", "Post-Election", "Overall"]
    selected_dataset = st.sidebar.selectbox("Select Dataset", dataset_options)


if __name__ == "__main__":
    sentiment()