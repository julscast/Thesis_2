import streamlit as st
import os


def topics():
    tab1, tab2, tab3, tab4 = st.tabs(['Pre-Election', 'During Election', 'Post-Election', 'Overall'])

    with tab1:
        pre_urls = [
            'images/Pre/1.png',
            'images/Pre/2.png',
            'images/Pre/3.png',
            'images/Pre/4.png']
        
        st.subheader("Pre-Election Topic Wordclouds")
        col1, col2 = st.columns(2)
        with col1:
            st.image(pre_urls[0], use_column_width=True)
        with col2:
            st.image(pre_urls[1], use_column_width=True)
        with col1:
            st.image(pre_urls[2], use_column_width=True)
        with col2:
            st.image(pre_urls[3], use_column_width=True)
    
    with tab2:
        dur_urls = [
            'images/During/1.png',
            'images/During/2.png',
            'images/During/3.png',
            'images/During/4.png']
        
        st.subheader("During Election Topic Wordclouds")
        col3, col4 = st.columns(2)
        with col3:
            st.image(dur_urls[0], use_column_width=True)
        with col4:
            st.image(dur_urls[1], use_column_width=True)
        with col3:
            st.image(dur_urls[2], use_column_width=True)
        with col4:
            st.image(dur_urls[3], use_column_width=True)

    with tab3:
        post_urls = [
            'images/Post/1.png',
            'images/Post/2.png',
            'images/Post/3.png',
            'images/Post/4.png']
        
        st.subheader("Post-Election Topic Wordclouds")
        col5, col6 = st.columns(2)
        with col5:
            st.image(post_urls[0], use_column_width=True)
        with col6:
            st.image(post_urls[1], use_column_width=True)
        with col5:
            st.image(post_urls[2], use_column_width=True)
        with col6:
            st.image(post_urls[3], use_column_width=True)

    with tab4:
        overall_urls = [
            'images/Overall/1.png',
            'images/Overall/2.png',
            'images/Overall/3.png',
            'images/Overall/4.png']
        
        st.subheader("Overall Topic Wordclouds")
        col7, col8 = st.columns(2)
        with col7:
            st.image(overall_urls[0], use_column_width=True)
        with col8:
            st.image(overall_urls[1], use_column_width=True)
        with col7:
            st.image(overall_urls[2], use_column_width=True)
        with col8:
            st.image(overall_urls[3], use_column_width=True)

if __name__ == "__main__":
    topics()