from pdf2docx import Converter


def convert_pdf_to_word(input_path, output_path):

    cv = Converter(input_path)

    cv.convert(output_path)

    cv.close()