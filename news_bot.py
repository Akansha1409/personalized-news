import os
import requests
from groq import Groq
from dotenv import load_dotenv

# Load keys
load_dotenv()
news_key = os.getenv("NEWS_API_KEY")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def fetch_news(topic="Artificial Intelligence"):
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&language=en&pageSize=5&apiKey={news_key}"
    response = requests.get(url).json()
    return response.get('articles', [])

def summarize_with_llama(headline, content):
    prompt = f"""
    Analyze this news item:
    Headline: {headline}
    Content Snippet: {content}
    
    Provide:
    1. A 1-sentence "Impact Summary".
    2. Sentiment Score (Scale -1 to 1).
    3. Importance (Low, Medium, High).
    """
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# Main Execution
print("🚀 Fetching the latest News...")
articles = fetch_news("NVIDIA AI") 

for i, art in enumerate(articles, 1):
    print(f"\n--- Article {i} ---")
    print(f"Original: {art['title']}")
    
    summary = summarize_with_llama(art['title'], art['description'])
    print(f"AI Architect Analysis:\n{summary}")