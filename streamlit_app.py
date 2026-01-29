import streamlit as st
from openai import OpenAI

# st.set_page_config MUST be first!
st.set_page_config(
    page_title="IST488 Homeworks", 
    page_icon=None, 
    layout="wide", 
    initial_sidebar_state="expanded", 
    menu_items=None
)

# Add the folder path to your lab files
hw1 = st.Page('HW/hw1.py', title='Homework One: incomplete')
hw2 = st.Page('HW/hw2.py', title='URL Summarizer with Multiple LLMs')

# Navigation and run
pg = st.navigation(pages=[hw1, hw2], position="sidebar", expanded=False)
pg.run()