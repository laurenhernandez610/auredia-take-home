# auredia-take-home


# 🤖 Predictive Planning & Scheduling Assistant

Welcome! This take-home assignment challenges you to build an AI-powered assistant that helps our teams understand delays, estimate delivery times, and surface key patterns — all in a usable interface.

---

## 📁 Dataset

You’ve been given 5 years of synthetic sales order data (~15,000 rows), located in the `data/` folder.

Each row contains:

- Order creation and delivery dates
- Region, product, and rep details
- Delay-related notes and status flags
- Pricing and shipment metadata

For a detailed breakdown of columns and expectations, see the full PDF brief below.

---

## 🧠 Project Overview

We want to see how you:

1. **Evaluate the data** and extract meaningful insights
2. **Enable LLM-powered Q&A**, giving users access to ask questions about order history or trends
3. **Predict delivery estimates** (time to completion or risk of delay)
4. **Explain the logic behind your predictions**
5. **Deliver a simple Streamlit UI** that ties it all together

---

## 🧪 Your Deliverables

### ✅ Core Requirements

- Clean and ingest the data
- Explore trends in delay frequency, causes, or regional patterns
- Train a predictive model (classification and/or regression)
- Integrate a lightweight **LLM-based Q&A assistant**
  - Use a free-tier or open-source LLM
  - Ground responses in the dataset (basic retrieval or summarization)
- Build a **Streamlit UI** that:
  - Accepts order inputs and shows predictions
  - Hosts the chatbot experience
  - Displays visual insights
  - Bonus for displaying why a prediction was made

---

## 📄 Instructions PDF

📄 [Click here to view the full project brief (PDF)](walkthrough/Planning%20%26%20Scheduling%20Assistant%20Project.pdf)

This file includes:

- Business context
- Column descriptions
- Your project goals
- Evaluation criteria

---

## 🧭 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the app
streamlit run app.py
```

📦 If you install any additional libraries during development, please add them to `requirements.txt` so we can run your app smoothly.
