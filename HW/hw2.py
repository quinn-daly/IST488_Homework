import streamlit as st

st.title("URL Summarizer with Multiple LLMs")

# Step 1: Just get a URL from the user
url = st.text_input("Enter a URL to summarize:", placeholder="https://example.com")

# Show what they entered (for testing)
if url:
    st.write(f"You entered: {url}")