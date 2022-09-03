# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:55:41 2022

@author: DELL
"""
import pickle
import streamlit as st
import requests
import bs4 as bs
import urllib.request
import pickle
import imdb
import numpy as np
ia = imdb.IMDb()



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    movie_title = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_title.append(movies.iloc[i[0]].title)

    return movie_title

## Implemented Using Streamlit

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    movie_title = recommend(selected_movie)
    print(movie_title)
    
    for i in range(5):
    
        col1,col2=st.columns(2)
        url = f"http://www.omdbapi.com/?t={movie_title[i]}&apikey=df3858f1"  
        re = requests.get(url)
        re = re.json()
        with col1:
            st.image(re['Poster'])
            with col2:
                st.subheader(re['Title'])
                st.caption(f"Genre: {re['Genre']}")
                st.caption(f"Year of Release: {re['Year']} ")
                st.write(re['Plot'])
                st.text(f"Language: {re['Language']}")
                st.text(f"IMDb Rating: {re['imdbRating']}")
                if re['imdbRating'] != 'N/A':
                    st.progress(float(re['imdbRating'])/10)
                st.text(f"Metacritic Rating: {re['Metascore']}")
                if re['Metascore'] != 'N/A':
                    st.progress(float(re['Metascore'])/100)
                result = ia.search_movie(movie_title[i])
                mv = result[0]
                chk_url = ia.get_imdbURL(mv)
                st.write("IMDb [link](%s)" % chk_url)
    
        
