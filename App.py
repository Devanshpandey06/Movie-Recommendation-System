import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommender", layout="wide")

# -------------------- Load Data --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/movies.csv")
    df['genres'] = df['genres'].fillna("")
    return df

movies = load_data()

# -------------------- Build Model --------------------
@st.cache_resource
def build_model():
    cv = CountVectorizer(tokenizer=lambda x: x.split("|"))
    genre_matrix = cv.fit_transform(movies['genres'])
    similarity = cosine_similarity(genre_matrix)
    return similarity

similarity = build_model()

# -------------------- Recommendation Function --------------------
def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return []

    idx = movies[movies['title'] == movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in sorted_scores]
    return recommended_movies

# -------------------- UI --------------------
st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get top 5 recommendations.")

selected_movie = st.selectbox(
    "Choose a movie:",
    sorted(movies['title'].tolist())
)

if st.button("Get Recommendations"):
    results = recommend(selected_movie)

    if results:
        st.subheader("Recommended Movies:")
        for m in results:
            st.write(f"✔ **{m}**")
    else:
        st.error("Movie not found in dataset!")
