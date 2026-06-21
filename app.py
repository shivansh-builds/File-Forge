
from flask import Flask, render_template, request, send_file
import os

from converters.pdf_to_word import convert_pdf_to_word
from converters.word_to_pdf import convert_word_to_pdf
from converters.merge_pdf import merge_pdfs
from converters.split_pdf import split_pdf

app = Flask(__name__)


# ==========================================
# Home Page
# ==========================================
# Create folders automatically
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# PDF to Word Converter
# ==========================================

@app.route("/pdf-to-word", methods=["GET", "POST"])
def pdf_to_word():

    if request.method == "POST":

        uploaded_file = request.files["pdf_file"]

        input_path = os.path.join(
            "uploads",
            uploaded_file.filename
        )

        uploaded_file.save(input_path)

        output_filename = uploaded_file.filename.replace(
            ".pdf",
            ".docx"
        )

        output_path = os.path.join(
            "outputs",
            output_filename
        )

        convert_pdf_to_word(
            input_path,
            output_path
        )

        return send_file(
            output_path,
            as_attachment=True
        )

    return render_template("pdf_to_word.html")


# ==========================================
# Word to PDF Converter
# ==========================================

@app.route("/word-to-pdf", methods=["GET", "POST"])
def word_to_pdf():

    if request.method == "POST":

        uploaded_file = request.files["word_file"]

        input_path = os.path.join(
            "uploads",
            uploaded_file.filename
        )

        uploaded_file.save(input_path)

        output_filename = uploaded_file.filename.replace(
            ".docx",
            ".pdf"
        )

        output_path = os.path.join(
            "outputs",
            output_filename
        )

        convert_word_to_pdf(
            input_path,
            output_path
        )

        return send_file(
            output_path,
            as_attachment=True
        )

    return render_template(
        "word_to_pdf.html"
    )


# ==========================================
# Merge PDF
# ==========================================

@app.route("/merge-pdf", methods=["GET", "POST"])
def merge_pdf():

    if request.method == "POST":

        uploaded_files = request.files.getlist(
            "pdf_files"
        )

        pdf_paths = []

        for file in uploaded_files:

            path = os.path.join(
                "uploads",
                file.filename
            )

            file.save(path)

            pdf_paths.append(path)

        output_path = os.path.join(
            "outputs",
            "merged.pdf"
        )

        merge_pdfs(
            pdf_paths,
            output_path
        )

        return send_file(
            output_path,
            as_attachment=True
        )

    return render_template(
        "merge_pdf.html"
    )


# ==========================================
# Split PDF
# ==========================================

@app.route("/split-pdf", methods=["GET", "POST"])
def split_pdf_route():

    if request.method == "POST":

        uploaded_file = request.files["pdf_file"]

        input_path = os.path.join(
            "uploads",
            uploaded_file.filename
        )

        uploaded_file.save(input_path)

        split_pdf(
            input_path,
            "outputs"
        )

        return "PDF split successfully. Check the outputs folder."

    return render_template(
        "split_pdf.html"
    )


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
