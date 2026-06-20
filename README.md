# 🤖 AI Resume RAG Chatbot

An AI-powered Resume Question Answering system built using **Flask**, **Google Gemini**, **Sentence Transformers**, and **ChromaDB**.

Upload your resume in PDF format and ask questions about your skills, experience, education, and projects. The chatbot uses Retrieval-Augmented Generation (RAG) to retrieve the most relevant parts of your resume before generating accurate responses with Google's Gemini model.

---

## 🚀 Features

* 📄 Upload resume (PDF)
* 🔍 Extract text using PyMuPDF
* ✂️ Split text into semantic chunks
* 🧠 Generate embeddings using Sentence Transformers
* 🗂️ Store embeddings in ChromaDB
* 🤖 Answer questions using Google Gemini
* 🎨 Clean and responsive web interface built with Flask

---

## 🛠️ Tech Stack

* Python
* Flask
* Google Gemini API
* ChromaDB
* Sentence Transformers
* PyMuPDF (fitz)
* HTML
* CSS

---

## 📂 Project Structure

```
resume-analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
│
├── uploads/
│
├── chroma_db/
│
└── utils/
    ├── pdf_reader.py
    ├── chunker.py
    ├── embeddings.py
    ├── chroma_db.py
    └── gemini.py
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Resume-RAG-Chatbot.git
cd Resume-RAG-Chatbot
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---



