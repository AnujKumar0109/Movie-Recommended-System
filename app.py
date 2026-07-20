
import pandas as pd
import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer


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



import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def stem(text):
    return " ".join(ps.stem(word) for word in text.split())

@st.cache_resource
def load_data():
    # Load movies dataframe
    movies = pickle.load(open("movies.pkl", "rb"))

    # Apply stemming
    movies["tags"] = movies["tags"].apply(stem)

    # Create vectors
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(movies["tags"]).toarray()

    # Compute similarity matrix
    similarity = cosine_similarity(vectors)

    return movies, similarity

movies, similarity = load_data()

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