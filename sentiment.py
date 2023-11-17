import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def selection(selected_dataset):
    if selected_dataset == "Pre-Election":
        return pd.read_csv("Datasets/SentimentAnalysis/Pre_Sentiment.csv")
    elif selected_dataset == "During Election":
        return pd.read_csv("Datasets/SentimentAnalysis/Dur_Sentiment.csv")
    elif selected_dataset == "Post-Election":
        return pd.read_csv("Datasets/SentimentAnalysis/Post_Sentiment.csv")
    elif selected_dataset == "Overall":
        return pd.read_csv("Datasets/SentimentAnalysis/Overall_Sentiment.csv")


def sentiment():
    dataset_options = ["Pre-Election", "During Election", "Post-Election", "Overall"]
    selected_dataset = st.sidebar.selectbox("Select Dataset", dataset_options)

    dataset = selection(selected_dataset)
    
    st.subheader(f"{selected_dataset} Tweets Sentiment Frequencies")
    col1, col2 = st.columns(2)


    #Bar Chart for Text Sentiments
    text_counts = dataset['Overall_Text_Sentiment'].value_counts()


    fig, ax = plt.subplots(figsize=(10, 6))
    colors = {'Negative': 'lightcoral', 'Neutral': 'lightgray', 'Positive': 'lightgreen'}

    positions = np.arange(len(text_counts))
    heights = text_counts.values
    
    bars = plt.bar(positions, heights, color=[colors[s] for s in text_counts.index])


    ax.set_title('Distribution of Overall Sentiment', fontsize=16)
    ax.set_xlabel('Sentiment', fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    ax.set_xticklabels(text_counts.index, rotation='horizontal', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    ax.set_xticks(positions)
    
    for position, height in zip(positions, heights):
        plt.text(position, height + 1, str(height), ha='center', va='bottom', fontsize=10)


    # Pie Chart for Text Sentiments
    text_counts_pie = dataset['Overall_Text_Sentiment'].value_counts()
    category = text_counts_pie.index


    fig_pie, ax_pie = plt.subplots()
    wedges, texts, autotexts = ax_pie.pie(text_counts_pie, labels=text_counts_pie.index,autopct='%1.1f%%', 
                                          startangle=90, colors=[colors[lab] for lab in category], pctdistance=0.85 )
    ax_pie.axis('equal')

    for autotext in autotexts:
        autotext.set_horizontalalignment('center')
        autotext.set_fontsize(10)

    with col1:
        st.pyplot(fig)
    
    with col2:
        st.pyplot(fig_pie)

    st.write("")

    st.subheader(f"{selected_dataset} Emojis Sentiment Frequencies")
    col3, col4 = st.columns(2)

    #Bar Chart for Emoji Sentiments
    emoji_counts = dataset['sentiment_class'].value_counts()
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    pos = np.arange(len(emoji_counts))
    hei = emoji_counts.values

    bar = plt.bar(pos, hei, color=[colors[x] for x in emoji_counts.index])

    ax2.set_title('Distribution of Overall Sentiment', fontsize=16)
    ax2.set_xlabel('Sentiment', fontsize=14)
    ax2.set_ylabel('Count', fontsize=14)
    ax2.set_xticklabels(emoji_counts.index, rotation='horizontal', fontsize=12)
    ax2.grid(axis='y', linestyle='--', alpha=0.7)

    ax2.set_xticks(pos)

    for post, heig in zip(pos, hei):
        plt.text(post, heig +1, str(heig), ha='center', va='bottom', fontsize=10)
    

    # Pie Chart for Text Sentiments
    emoji_counts_pie = dataset['sentiment_class'].value_counts()
    emojicategory = emoji_counts_pie.index


    fig_pie2, ax_pie2 = plt.subplots()
    wedges2, texts2, autotexts2 = ax_pie2.pie(emoji_counts_pie, labels=emoji_counts_pie.index,autopct='%1.1f%%', 
                                          startangle=90, colors=[colors[lab] for lab in emojicategory], pctdistance=0.85 )
    ax_pie2.axis('equal')

    for autotext2 in autotexts2:
        autotext2.set_horizontalalignment('center')
        autotext2.set_fontsize(10)


    with col3:
        st.pyplot(fig2)

    with col4:
        st.pyplot(fig_pie2)


if __name__ == "__main__":
    sentiment()