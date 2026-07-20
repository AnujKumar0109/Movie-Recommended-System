# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Live Demo

🌐 **Live Application**

https://movie-recommendation-syystemm.streamlit.app

---

# 📖 Project Overview

This is a **Content-Based Movie Recommendation System** built using **Python**, **Streamlit**, and **Machine Learning**.

The application recommends movies similar to a selected movie by analyzing:

- Genres
- Cast
- Crew
- Keywords
- Movie Overview

The recommendation engine uses **CountVectorizer** and **Cosine Similarity** to find the most similar movies.

---

# ✨ Features

- 🎥 Movie recommendations
- 🤖 Content-based recommendation system
- ⚡ Fast recommendation generation
- 🎨 Beautiful Streamlit UI
- 📚 Preprocessed movie dataset
- 💻 Responsive interface
- 🚀 Easy deployment

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| NLTK | Text Stemming |

---

# 📂 Project Structure

```text
Movie-Recommended-System/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── images/
    ├── home.png
    └── recommendation.png
```

> **Note:** The similarity matrix is generated automatically when the application starts. No separate `similarity.pkl` file is required.

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/AnujKumar0109/Movie-Recommended-System.git
```

Move into the project directory

```bash
cd Movie-Recommended-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# ▶️ Usage

1. Launch the application.
2. Select a movie.
3. Click **Recommend Movies**.
4. View the recommendations.

---

# 📸 Screenshots

## Home Page

![Home](images/home.png)

## Recommendations

![Recommendations](images/recommendation.png)

---

# 📊 Dataset

The dataset contains movie information including:

- Movie Titles
- Genres
- Keywords
- Cast
- Crew
- Overview

The recommendation engine creates feature vectors using **CountVectorizer** and calculates movie similarity using **Cosine Similarity**.

---

# ☁️ Deployment

The project is deployed on **Streamlit Community Cloud**.

To deploy your own copy:

1. Fork this repository.
2. Login to Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select this repository.
5. Choose **app.py** as the main file.
6. Deploy.

---

# 🚀 Future Improvements

- ⭐ Movie posters
- ⭐ Movie ratings
- ⭐ TMDB API integration
- ⭐ Genre filtering
- ⭐ Search autocomplete
- ⭐ Hybrid recommendation system
- ⭐ User authentication

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a branch

```bash
git checkout -b feature-name
```

3. Commit

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 👨‍💻 Author

**Anuj Kumar**

📧 Email: choudharyneeju990@gmail.com

💻 GitHub: https://github.com/AnujKumar0109

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

---

# 📜 License

This project is licensed under the MIT License.
