from flask import Flask, render_template, request, send_file
import os

from converters.pdf_to_word import convert_pdf_to_word

app = Flask(__name__)


# ==========================
# Home Page
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# PDF to Word Converter
# ==========================

@app.route("/pdf-to-word", methods=["GET", "POST"])
def pdf_to_word():

    if request.method == "POST":

        uploaded_file = request.files["pdf_file"]

        # Save uploaded PDF
        input_path = os.path.join(
            "uploads",
            uploaded_file.filename
        )

        uploaded_file.save(input_path)

        # Create output filename
        output_filename = uploaded_file.filename.replace(
            ".pdf",
            ".docx"
        )

        output_path = os.path.join(
            "outputs",
            output_filename
        )

        # Convert PDF to Word
        convert_pdf_to_word(
            input_path,
            output_path
        )

        # Download converted file
        return send_file(
            output_path,
            as_attachment=True
        )

    return render_template("pdf_to_word.html")


# ==========================
# Run Application
# ==========================

if __name__ == "__main__":
    app.run(debug=True)