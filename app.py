import streamlit as st
import os
import requests
from groq import Groq

# Page Setup
st.set_page_config(page_title="AI News Architect", page_icon="📰")
st.title("📰 AI Personalized News Architect")
st.markdown("Summarizing the world's news using **Llama 3.3**")

# Sidebar for API Keys (Or use Secrets)
with st.sidebar:
    st.header("Settings")
    topic = st.text_input("Enter Topic", value="Artificial Intelligence")
    num_articles = st.slider("Number of Articles", 1, 10, 5)

# Initialize Groq & NewsAPI (Pulling from Streamlit Secrets)
# When deploying, we will add these to Streamlit's "Secrets" panel
NEWS_KEY = st.secrets["NEWS_API_KEY"]
GROQ_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_KEY)

if st.button("Generate News Report"):
    with st.spinner("Fetching and analyzing news..."):
        # 1. Fetch News
        url = f"https://newsapi.org/v2/everything?q={topic}&pageSize={num_articles}&language=en&apiKey={NEWS_KEY}"
        data = requests.get(url).json()
        articles = data.get('articles', [])

        if not articles:
            st.warning("No articles found for this topic.")
        
        for art in articles:
            st.subheader(art['title'])
            st.caption(f"Source: {art['source']['name']} | Published: {art['publishedAt']}")
            
            # 2. LLM Analysis
            prompt = f"Summarize this news headline and snippet into one powerful sentence and give it an importance score (Low/Medium/High): \nHeadline: {art['title']} \nSnippet: {art['description']}"
            
            completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
            )
            
            analysis = completion.choices[0].message.content
            st.info(f"**AI Analysis:** {analysis}")
            st.divider()