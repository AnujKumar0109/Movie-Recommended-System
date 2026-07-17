import streamlit as st
import pickle
import pandas as pd

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# Load Data
# ==========================================
movie_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# ==========================================
# Recommendation Function
# ==========================================
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for movie_data in movies_list:
        recommended_movies.append(
            movies.iloc[movie_data[0]].title
        )

    return recommended_movies


# ==========================================
# Sidebar
# ==========================================
st.sidebar.title("ℹ️ About")

st.sidebar.info(
    """
### Movie Recommender System

This application recommends movies similar to your selected movie using a **Content-Based Recommendation System**.

**Tech Stack**
- Python
- Streamlit
- Pandas
- Machine Learning

Developed by **Anuj Kumar**
"""
)

# ==========================================
# Main Title
# ==========================================
st.title("🎬 Movie Recommender System")

st.markdown(
    """
Discover movies similar to your favorite films using a
**Content-Based Recommendation System**.
"""
)

st.divider()

# ==========================================
# Movie Selection
# ==========================================
selected_movie_name = st.selectbox(
    "🎥 Select a Movie",
    movies["title"].values
)

# ==========================================
# Recommendation Button
# ==========================================
if st.button("🎯 Recommend Movies", use_container_width=True):

    recommendations = recommend(selected_movie_name)

    st.subheader("🍿 Recommended Movies")

    cols = st.columns(5)

    for i, movie in enumerate(recommendations):
        with cols[i]:
            st.success(movie)