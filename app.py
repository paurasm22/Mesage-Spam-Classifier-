import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer

ps = PorterStemmer()
tokenizer = TreebankWordTokenizer()  # DOES NOT require punkt_tab

nltk.download('stopwords')  # only stopwords needed

def transform_text(text):
    text = text.lower()
    text = tokenizer.tokenize(text)  # FIXED

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.error("🚨 Spam")
    else:
        st.success("✔ Not Spam")
