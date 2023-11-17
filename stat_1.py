import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter
    
def stats():
    tab1, tab2 = st.tabs(["Raw Data","Cleaned Data"])

    def extract_hashtags(text):
        # Use regular expression to extract hashtags
        hashtags = re.findall(r'#\w+', text)
        return hashtags
    
    with tab1:
        st.header('Raw Data Statistics')
        raw_df = pd.read_csv('Datasets/RawTweets.csv')
        col1, col2 = st.columns(2)

        # Number of Tweets per Election Phase
        
        frequency_table = pd.DataFrame(raw_df['Period'].value_counts()).reset_index()
        frequency_table.columns = ['Period','Frequency']

        total_row = pd.DataFrame({"Period": ['Total', ], 'Frequency': [frequency_table['Frequency'].sum()]})
        
        frequency_table_wtotal = pd.concat([frequency_table, total_row], ignore_index=True)
        
        custom_order = ['PRE', 'DUR', 'POST', 'Total']
        frequency_table_wtotal['Period'] = pd.Categorical(frequency_table_wtotal['Period'], categories=custom_order, ordered=True)
        frequency_table_wtotal = frequency_table_wtotal.sort_values(by='Period')

        updated_names = ['Pre-Election', 'During Election', 'Post-Election', 'Total']
        frequency_table_wtotal['Period'] = updated_names

        frequency_table_wtotal.reset_index(drop=True, inplace=True)

        #Number of Tweets Based on Hashtag
        all_hashtags = raw_df['Tweet'].apply(extract_hashtags).explode().str.lower()
        hashtag_counts = Counter(all_hashtags)
        top_hashtags = dict(hashtag_counts.most_common(5))
        df_top_hashtags = pd.DataFrame(list(top_hashtags.items()), columns=['Hashtag', 'Count'])

        with col1:
            st.subheader("Number of Tweets per Election Phase")
            st.table(frequency_table_wtotal)
            st.subheader("Number of Tweets based on Hashtags Used")
            st.table(df_top_hashtags)

        
        #Pie Chart for Phase %
        frequency_table_for_pie = pd.DataFrame(frequency_table)

        custom_order2 = ['PRE','DUR','POST']
        frequency_table_for_pie['Period'] = pd.Categorical(frequency_table_for_pie['Period'], categories=custom_order2, ordered=True)
        frequency_table_for_pie = frequency_table_for_pie.sort_values(by='Period')
        
        updated_names2 = ['Pre-Election', 'During Election', 'Post-Election']
        frequency_table_for_pie['Period'] = updated_names2

        fig, ax = plt.subplots()
        ax.pie(frequency_table_for_pie['Frequency'],labels=frequency_table_for_pie['Period'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        with col2:
            st.subheader("Number of Tweets by Election Phase in %")
            st.pyplot(fig, clear_figure=True, use_container_width=True)

        st.write("")
        
        #Line Chart for Dates
        col3 = st.columns(1)[0]
        with col3:
            st.subheader("Number of Tweets Gathered per Day")
            dates = raw_df['Date'].value_counts().sort_index()
            dates.index = pd.to_datetime(dates.index)
            dates.index = dates.index.strftime('%b %d')
            dates = dates.sort_index()
            st.line_chart(dates)


    # CLEANED DATA TAB
    with tab2:
        st.header('Cleaned Data Statistics')
        clean_df = pd.read_csv('Datasets/CleanedTweets.csv')
        column1, column2 = st.columns(2)

        #Number of Tweets per Election Phase

        fq_table = pd.DataFrame(clean_df['Period'].value_counts()).reset_index()
        fq_table.columns = ['Period','Frequency']

        tot_row = pd.DataFrame({"Period": ['Total', ], 'Frequency': [fq_table['Frequency'].sum()]})

        fq_table_wtotal = pd.concat([fq_table,tot_row], ignore_index=True)

        cus_order = ['PRE', 'DUR', 'POST', 'Total']
        fq_table_wtotal['Period'] = pd.Categorical(fq_table_wtotal['Period'], categories=cus_order, ordered=True)
        fq_table_wtotal = fq_table_wtotal.sort_values(by='Period')

        #updated_names = ['Pre-Election', 'During Election', 'Post-Election', 'Total']
        fq_table_wtotal['Period'] = updated_names

        fq_table_wtotal.reset_index(drop=True, inplace=True)

        #Number of Duplicate Tweets
        dup_df = {
            'Election Phase' : ['Pre-Election','During Election','Post-Election'],
            'Raw Dataset': pd.Series([5011, 4991, 6641]),
            'Cleaned Dataset': pd.Series([3835, 3681, 5771])
        }
        dup_df = pd.DataFrame(dup_df)
        dup_df['Duplicate Tweets'] = dup_df['Raw Dataset'] - dup_df['Cleaned Dataset']
    
        sums = dup_df[['Raw Dataset','Cleaned Dataset','Duplicate Tweets']].sum()
        dup_df.loc[len(dup_df)] = ['Total', sums['Raw Dataset'], sums['Cleaned Dataset'], sums['Duplicate Tweets']]
        # sum_row = pd.DataFrame({'Election Phase': 'Total', 'Raw Dataset':sums['Raw Dataset'], 'Cleaned Dataset':sums['Cleaned Dataset'], 'Duplicate Tweets':sums['Duplicate Tweets']})

        # dup_df = pd.concat([dup_df, sum_row], ignore_index=True)
        
        with column1:
            st.subheader("Number of Tweets per Election Phase")
            st.table(fq_table_wtotal)
            st.subheader("Comparison of Number of Tweets")
            st.table(dup_df)

        #Pie Chart for Phase %
        fq_table_for_pie = pd.DataFrame(fq_table)

        # custom_order = ['PRE', 'DUR', 'POST']
        fq_table_for_pie['Period'] = pd.Categorical(fq_table_for_pie['Period'], categories=custom_order2, ordered=True)
        fq_table_for_pie = fq_table_for_pie.sort_values(by='Period')

        fq_table_for_pie['Period'] = updated_names2

        fig2, ax2 = plt.subplots()
        ax2.pie(fq_table_for_pie['Frequency'], labels=fq_table_for_pie['Period'], autopct='%1.1f%%', startangle=90)
        ax2.axis('equal')

        with column2:
            st.subheader("Number of Tweets by Election Phase in %")
            st.pyplot(fig2, clear_figure=True, use_container_width=True)

        st.write("")

        #Line Chart for Dates
        column3 = st.columns(1)[0]
        with column3:
            st.subheader("Number of Tweets Gathered per Day")
            dates2 = clean_df['Date'].value_counts().sort_index()
            dates2.index = pd.to_datetime(dates2.index)
            dates2.index = dates2.index.strftime('%b %d')
            dates2 = dates2.sort_index()
            st.line_chart(dates2)

if __name__ == "__main__":
    stats()