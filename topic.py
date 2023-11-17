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


dataset_options = ["Pre-Election", "During Election", "Post Election", "Overall"]
selected_dataset = st.sidebar.selectbox("Select Dataset", dataset_options)

# def load_dataset(dataset_name):
#     if dataset_name == "Pre Election":
#     elif dataset_name == "During Election":
#     elif dataset_name == "Post Election":
#     elif dataset_name == "Overall":
#         dataset=pd.read_csv("Datasets/TopicModels/")
# return data

def topic():
 
    #Wordcloud to visualize first
    st.subheader("Wordcloud")
    
    long_string = ','.join(list(dataset['Corrected_Words'].values))
    wordcloud = WordCloud(background_color="white", max_words=50, contour_width=3, contour_color='steelblue',width=1000, height=500)
    wordcloud = wordcloud.generate(long_string)
    wordcloud = wordcloud.to_image()

    

    #Start of Topic Modeling
    documents = dataset['Corrected_Words'].values
    tokenized_documents = [doc.split(",") for doc in documents] 

    #Create Dictionary
    id2word = corpora.Dictionary(tokenized_documents)

    #Create Corpus
    texts = tokenized_documents

    #Term Document Frequency
    corpus = [id2word.doc2bow(doc) for doc in tokenized_documents]

    #Build the LDA model
    num_topics = 4 
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=num_topics, passes=15,
                                                random_state=42,chunksize=50,per_word_topics=True)
    
    
    #Coherence Score
    coherence_model_lda = CoherenceModel(model=lda_model, texts=tokenized_documents, dictionary=id2word, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()

    #Topic Modeling Visualization
    cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]
    cloud = WordCloud(background_color='white', width=2500, height=2800, max_words=20,
                            colormap='tab10', color_func=lambda * args, **kwargs: cols[i],
                            prefer_horizontal=1.0)

    topics = lda_model.show_topics(formatted=False)

    fig, axes = plt.subplots(2,2, figsize=(20,10), sharex=True, sharey=True)

    for i, ax in enumerate(axes.flatten()):
        fig.add_subplot(ax)
        topic_words = dict(topics[i][1])
        cloud.generate_from_frequencies(topic_words,max_font_size=300)
        plt.gca().imshow(cloud)
        plt.gca().set_title('Topic '+ str(i), fontdict=dict(size=16))
        plt.gca().axis('off')

    plt.subplots_adjust(wspace=0, hspace=0.1)
    plt.axis('off')
    plt.margins(x=0,y=0)
    plt.tight_layout
    plt.show()