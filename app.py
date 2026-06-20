from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

from utils.pdf_reader import extract_text
from utils.chunker import split_text
from utils.rag import create_vectorstore, search_resume
from utils.gemini import ask_gemini

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return render_template(
            "index.html",
            error="No file selected."
        )

    file = request.files["resume"]

    if file.filename == "":
        return render_template(
            "index.html",
            error="Please choose a PDF."
        )

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    print("\nUploading:", file.filename)

    resume_text = extract_text(filepath)

    print("\nExtracted Characters:", len(resume_text))
    print(resume_text[:1000])

    chunks = split_text(resume_text)

    print("\nChunks Created:", len(chunks))

    create_vectorstore(chunks)

    return render_template(
        "index.html",
        uploaded=True,
        filename=file.filename
    )


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form.get("question")

    if not question:

        return render_template(
            "index.html",
            error="Please enter a question."
        )

    docs = search_resume(question)

    if len(docs) == 0:

        return render_template(
            "index.html",
            uploaded=True,
            question=question,
            answer="❌ No relevant information found in the uploaded resume."
        )

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    print("\nContext Sent to Gemini:\n")
    print(context)

    answer = ask_gemini(question, context)

    return render_template(
        "index.html",
        uploaded=True,
        question=question,
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)