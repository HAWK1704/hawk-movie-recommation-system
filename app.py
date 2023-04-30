import streamlit as st
import pandas as pd
import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d575cdc4c8d8433f1957185fd39b2597&language=en-US'.format(movie_id)).json()
    return 'https://image.tmdb.org/t/p/w500/'+response['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommended_movies_poster
movies=pd.read_pickle('movies.pkl')
similarity=pd.read_pickle('similarity.pkl')
st.title('Movie Recommender System')
selected_movie_name =st.selectbox('Select the movies you watched...',movies['title'])
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
