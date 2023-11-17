import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from wordcloud import WordCloud
import gensim
from gensim import corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from gensim.test.utils import common_corpus, common_dictionary
from gensim.models.ldamodel import LdaModel
from gensim.models.coherencemodel import CoherenceModel

def load_dataset(dataset_name):

    if dataset_name == "Pre-Election":
        return pd.read_csv("Datasets/TopicModeling/Pre_Topic.csv")
    elif dataset_name == "During Election":
        return pd.read_csv("Datasets/TopicModeling/Dur_Topic.csv")
    elif dataset_name == "Post-Election":
        return pd.read_csv("Datasets/TopicModeling/Post_Topic.csv")
    elif dataset_name == "Overall":
        return pd.read_csv("Datasets/TopicModeling/Overall_Topic.csv")
    

def topics():

    dataset_options = ["Pre-Election", "During Election", "Post-Election", "Overall"]
    selected_dataset = st.sidebar.selectbox("Select Dataset", dataset_options)
    
    dataset = load_dataset(selected_dataset)

    

if __name__ == "__main__":
    topics()