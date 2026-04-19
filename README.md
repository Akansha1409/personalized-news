# 📰 Personalized News Architect (AI-Agent)

[![Live Demo](https://img.shields.io/badge/Demo-Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit)](https://ak1409-personalized-news.hf.space)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Llama 3.3](https://img.shields.io/badge/Model-Llama_3.3-04100b?style=for-the-badge&logo=meta)](https://groq.com/)
[![Groq](https://img.shields.io/badge/Inference-Groq_Fast-f55036?style=for-the-badge&logo=fastapi)](https://groq.com/)

## 📌 Project Overview
The **Personalized News Architect** is an automated intelligence pipeline that solves information overload. It doesn't just fetch news; it acts as an **AI Agent** that scrapes real-time headlines, performs sentiment analysis, and generates high-signal 1-sentence summaries using **Llama 3.3** via the **Groq API**.

### 🧠 Why this matters:
In a world of constant notification noise, this tool filters thousands of headlines into a single, personalized daily briefing. It demonstrates the use of **Agentic AI**—moving beyond simple chatbots to systems that handle data fetching, reasoning, and synthesis automatically.

---

## 📊 Research & Data Insights
> **Exploratory Data Analysis (Jupyter Notebook)**
> *Analyzed 50+ live articles to identify source dominance and publication trends.*

![Media Landscape Chart](URL_TO_YOUR_SCREENSHOT_HERE)

### **Key Features:**
- **Automated Aggregation:** Connects to **NewsAPI** to pull the latest headlines across any topic (AI, Finance, Sports).
- **LLM Synthesis:** Uses **Llama 3.3 (70B)** to condense long articles into actionable "Impact Summaries."
- **Sentiment Scoring:** Automatically flags articles as High/Medium/Low importance based on linguistic impact.
- **Real-Time UI:** A **Streamlit** dashboard for on-demand intelligence reports.

---

## 🛠️ Technical Stack

| Category | Technology Used |
| :--- | :--- |
| **Programming Language** | Python 3.13 |
| **Generative AI Model** | Llama 3.3 (70B) |
| **Inference Engine** | Groq Cloud API |
| **Data Retrieval** | NewsAPI (REST API) |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Web Framework** | Streamlit |
| **Environment** | Dotenv, Virtual Environments |

---

```

## 📁 Project Structure
```text
├── analysis.ipynb        # Data Research (50-article fetch + Charts)
├── app.py                # Streamlit Live Web Application
├── news_bot.py           # Core AI Engine (API logic & Prompting)
├── .env.example          # Template for API keys (NewsAPI & Groq)
└── requirements.txt      # Project dependencies
