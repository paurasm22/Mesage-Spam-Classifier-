📩 SMS / Email Spam Classifier
📝 Description

This project is a machine learning–based web application that classifies messages as Spam or Not Spam.
It uses NLP preprocessing, TF-IDF vectorization, and a Multinomial Naive Bayes model.
A simple Streamlit interface allows users to type a message and instantly get a prediction.

🌐 Live App

Paste your deployed link here.

📘 Project Overview

The classifier is trained on a labeled SMS dataset and uses the following NLP steps:

• Text cleaning and tokenization
• Removing stopwords and punctuation
• Stemming using PorterStemmer
• Converting text into numerical vectors using TF-IDF

The model predicts whether the message is Spam or Not Spam.
The project is lightweight and deployable on Streamlit Cloud or Hugging Face Spaces.

✨ Features

• Real-time spam prediction
• Clean and simple UI
• Custom NLP preprocessing pipeline
• Lightweight and fast ML model
• Free deployment options

📂 Project Structure

Includes:

• Streamlit app file
• Trained Naive Bayes model
• TF-IDF vectorizer
• Requirements file
• Documentation

🔧 Installation

(These are the only code blocks.)

Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

🚀 Deployment

Easily deploy on:

• Streamlit Cloud
• Hugging Face Spaces

Upload:
app.py, model.pkl, vectorizer.pkl, requirements.txt.
