import streamlit as st

st.set_page_config(page_title="About | Movie Recommender")

# -------------------- Custom CSS --------------------
st.markdown("""
<style>

body {
    background-color: #0f0f0f;
}

.section {
    background-color: #1a1a1a;
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 25px;
    box-shadow: 0px 0px 10px #222;
    border: 1px solid #333;
}

.heading {
    font-size: 28px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 5px;
}

.sub {
    font-size: 18px;
    font-weight: 300;
    color: #cccccc;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    grid-gap: 20px;
    margin-top: 20px;
}

.card {
    background-color: #121212;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0px 0px 8px #333;
    border: 1px solid #2e2e2e;
    text-align: center;
}

.card-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 12px;
    color: #fff;
}

.card-desc {
    font-size: 15px;
    color: #bbbbbb;
}

.footer {
    margin-top: 40px;
    text-align: center;
    color: #777;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- Main UI --------------------
st.title("🎬 About This Project")
st.write("")
st.markdown(
    '<div class="sub">A smart movie recommendation system powered by machine learning and Streamlit.</div>',
    unsafe_allow_html=True
)

# -------------------- Section 1 --------------------
st.markdown("""
<div class="section">
    <div class="heading">📌 Project Objective</div>
    <div class="sub">
        This system suggests movies based on similarity of genres using
        <b>Content-Based Filtering</b>.  
        It analyzes movie metadata and matches patterns to deliver accurate recommendations.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------- Section 2 --------------------
with st.container():
    st.markdown("""
    <div class="section">
        <div class="heading">🛠️ Technologies Used</div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4, gap="small")
    tech_cards = [
        ("https://cdn-icons-png.flaticon.com/512/919/919852.png", "Python", "Core scripting language for model & logic."),
        ("https://pandas.pydata.org/static/img/pandas_secondary.svg", "Pandas", "Data cleaning, merging and transformation."),
        ("https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png", "Scikit-Learn", "Cosine Similarity & vectorization."),
        ("https://upload.wikimedia.org/wikipedia/commons/0/0a/Streamlit_Logo_1.png", "Streamlit", "Frontend UI for interactive recommendations.")
    ]

    for col, (img, title, desc) in zip(cols, tech_cards):
        with col:
            st.image(img, width=55)
            st.markdown(f'<div class="card-title">{title}</div><div class="card-desc">{desc}</div>', unsafe_allow_html=True)

# -------------------- Section 3 --------------------
st.markdown("""
<div class="section">
    <div class="heading">🎯 How It Works</div>
    <div class="sub">
        <b>Step 1:</b> Extract movie genres <br>
        <b>Step 2:</b> Convert genres to numerical vectors <br>
        <b>Step 3:</b> Compute similarity using <b>Cosine Similarity</b> <br>
        <b>Step 4:</b> Recommend top 5 similar movies <br><br>
        The system can be easily extended to support collaborative filtering, hybrid filtering, and sentiment analysis.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------- Section 4 --------------------
st.markdown("""
<div class="section">
    <div class="heading">👨‍💻 Developer</div>
    <div class="sub">
        Designed & developed by <b>Devansh Pandey</b>.  
        Passionate about Python, Machine Learning, and creating smart systems.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------- Footer --------------------
st.markdown("""
<div class="footer">
    © 2025 Movie Recommendation System • Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
