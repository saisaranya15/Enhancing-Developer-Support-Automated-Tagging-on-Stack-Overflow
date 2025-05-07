import streamlit as st
from PIL import Image

# Set background color for the entire page
st.markdown(
    """
    <style>
        .stApp {
            background-color: #E6E6FA; /* Soft Pastel Green */
        }
        .blue-box {
            background-color: white; /* White Background */
            color: black;
            padding: 10px;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# Title
st.title("Automated Tagging on Stack Overflow")

# Problem Statement
st.markdown('<div class="blue-box">Business Problem</div>', unsafe_allow_html=True)
st.write("""
Stack Overflow is one of the largest Q&A platforms for programmers, where users post questions on various programming topics.
To facilitate better searchability and categorization, each question is assigned relevant tags that describe its content (e.g., `python`, `machine-learning`, `web-development`).

However, many users may struggle to assign the most appropriate tags, leading to misclassification or difficulty in retrieving relevant content.

**This project aims to build a machine learning model that can automatically predict the relevant tags for a given Stack Overflow question based on its title and description.**
This will enhance user experience, improve content organization, and reduce the need for manual intervention in tag assignment.
""")

# Business Objective
st.markdown('<div class="blue-box">Business Objective</div>', unsafe_allow_html=True)
st.write("""
The goal of this project is to **automate the tag assignment process** for Stack Overflow questions by developing a machine learning model that can predict the most relevant tag(s) based on the question’s title and body (description).

This addresses the following business needs:

- **Improved Searchability**: Accurate tags make it easier for users to find relevant questions and answers.
- **Enhanced User Experience**: Reduces the burden on users to manually assign correct tags.
- **Content Organization**: Helps maintain a well-structured, searchable, and consistent knowledge base.
""")

# Data Understanding
st.markdown('<div class="blue-box">Data Understanding</div>', unsafe_allow_html=True)
st.write("""
The dataset contains the following columns:

| Column Name | Description |
|-------------|-------------|
| `title`     | The headline or subject of the Stack Overflow question (short summary). Usually contains keywords. |
| `body`      | The detailed description of the question, including code snippets, error messages, and contextual info. Rich in technical content. |
| `tags`      | The target variable. Represents the topic(s) associated with the question. These can be single or multiple tags like `python`, `pandas`, `machine-learning`, etc. |
""")

