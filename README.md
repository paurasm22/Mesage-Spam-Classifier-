

````markdown
# 📩 SMS / Email Spam Classifier  
A machine learning web application that detects whether a message is **Spam** or **Not Spam** using NLP techniques and a Multinomial Naive Bayes model.  
This project is inspired by the CampusX spam classifier tutorial.

---

## 🚀 Live Demo  
🔗 **App Link:** *https://paurasspamclassifier.streamlit.app/*

---

## 📘 Project Overview  
This project classifies SMS or Email messages into:

- **Spam**
- **Not Spam (Ham)**

It uses:
- Text preprocessing (lowercasing, tokenizing, stopword removal, stemming)
- TF-IDF Vectorization  
- Multinomial Naive Bayes classification  
- Streamlit UI for real-time prediction  

---

## 🧠 Features  
✔ Clean & simple UI  
✔ Real-time spam prediction  
✔ Custom text preprocessing pipeline  
✔ Efficient ML model (Naive Bayes)  
✔ Fully deployed using Streamlit/HuggingFace  

---

## 🧪 Tech Stack  

### **Frontend / UI**
- Streamlit

### **Backend / ML**
- Python
- Scikit-learn
- NLTK
- TF-IDF Vectorizer
- Multinomial Naive Bayes

---

## 🛠️ Installation & Usage (Local Setup)

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
````

### 2️⃣ Install dependencies

Create a virtual environment (recommended):

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
📁 Spam-Classifier/
│── app.py                 # Streamlit UI
│── model.pkl              # Trained Naive Bayes model
│── vectorizer.pkl         # TF-IDF Vectorizer
│── requirements.txt       # Project dependencies
│── README.md              # Project documentation
```

---

## 🔍 How It Works

### 1️⃣ Preprocessing (Custom NLP pipeline)

* Lowercasing
* Tokenization
* Removing special characters
* Removing stopwords
* Stemming using PorterStemmer

### 2️⃣ Vectorization

* TF-IDF converts text into numerical features

### 3️⃣ Model

* Multinomial Naive Bayes
* Performs well on text classification tasks

### 4️⃣ Prediction

The model outputs:

* **1 → Spam**
* **0 → Ham**

---

## 📦 Deployment

This project can be deployed on:

### ✔ Streamlit Cloud (Recommended)

Just connect your GitHub repo → Deploy.

### ✔ Hugging Face Spaces

Create a new Space → Choose Streamlit → Upload files.

---

## 🧾 Requirements

```
streamlit
scikit-learn
nltk
numpy
pandas
```

## 📜 License

This project is free to use for educational and personal purposes.

