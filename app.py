"""
Streamlit app entry point.

Suggested structure:
- Load cleaned data
- Route between delay exploration, prediction, and chat
- Tie together the interface and backend logic
"""

import streamlit as st
# from src.ingest import DataIngestor
# from src.explore import DataExplorer
# from src.model import DelayPredictor
# from src.llm import LLMChatbot

st.set_page_config(page_title="Planning & Scheduling Assistant")
st.title("📦 Planning & Scheduling Assistant")

# === Step 1: Load and clean data ===
# ingestor = DataIngestor('data/sales_data.csv')
# df = ingestor.load_and_clean()

# === Step 2: Initialize core modules ===
# explorer = DataExplorer(df)
# predictor = DelayPredictor()
# llm = LLMChatbot()

# === Step 3: Sidebar mode selection ===
# mode = st.sidebar.radio("Choose a mode", ['Explore Delay Trends', 'Predict Delivery Outcome', 'Ask the Assistant'])

# === Step 4: Route based on selected mode ===
# if mode == 'Explore Delay Trends':
#     st.subheader("📊 Delay Trend Insights")
#     # TODO: Call explorer methods to display charts and summaries

# elif mode == 'Predict Delivery Outcome':
#     st.subheader("🔮 Delivery Predictor")
#     # TODO: Accept user input, call predictor.predict(), and display output

# elif mode == 'Ask the Assistant':
#     st.subheader("💬 Ask a Question")
#     # TODO: Add user text input, pass to LLMChatbot.ask(), and display the response