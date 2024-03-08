# Run this file

# To work on your Flask application code in Visual Studio Code (VS Code), you can use several extensions that can enhance your development experience. Here are some recommended extensions for working with Flask projects in VS Code:

# Python: Install the official Python extension by Microsoft for Python development. It provides features like code completion, debugging, and linting.

# Flask Snippets: This extension provides snippets for Flask that can help you quickly generate Flask code constructs like routes, templates, and forms.

# HTML Snippets: Although not specific to Flask, this extension can be helpful for generating HTML code quickly, especially when working with Flask templates.

# Pylance: This extension enhances the Python development experience in VS Code by providing advanced code analysis, type checking, and auto-completions.

# GitLens: If you're using Git for version control, GitLens is a powerful extension that adds Git-related features to your editor, making it easier to work with version control.

# Markdown All in One: If you plan to include documentation or README files, this extension is handy for editing Markdown documents.

# AutoDocstring: This extension simplifies the process of adding docstrings to your Python functions and classes.

# REST Client: If you are working on an API-based Flask application, the REST Client extension can be helpful for testing API endpoints directly from VS Code.

# Docker: If you plan to containerize your Flask application, the Docker extension can assist with managing Docker containers and images.

# SQLite: If you are using SQLite as your database for the Flask application, the SQLite extension helps you interact with SQLite databases directly from VS Code.

# To install these extensions, follow these steps:

# Open VS Code.

# Go to the Extensions view by clicking on the square icon on the left sidebar.

# Search for the extensions mentioned above and install them.

# After installation, you may need to configure some extensions to suit your preferences or project requirements. You can access extension settings via the gear icon in the Extensions view.

# These extensions should help you effectively develop, debug, and manage your Flask application code within VS Code.


import os
import fitz  # PyMuPDF
from PIL import Image, ImageFilter
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Get the base name of the uploaded PDF file without extension
        pdf_file_name = os.path.splitext(file.filename)[0]

        # Save the uploaded PDF file
        pdf_file_path = os.path.join("result/uploads", f"{pdf_file_name}.pdf")
        file.save(pdf_file_path)

        # Open the PDF file
        doc = fitz.open(pdf_file_path)

        # Extract text from the PDF
        extracted_text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            extracted_text += page.get_text("text")

        # Save the extracted text to a text file with the same name as the PDF file
        text_file_path = os.path.join("result/data/", f"{pdf_file_name}.txt")
        with open(text_file_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)

        # Create a folder to save the extracted images
        output_folder = f"result/images/{pdf_file_name}_extracted_images"
        os.makedirs(output_folder, exist_ok=True)

        # Extract images from the PDF
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            xobjects = page.get_images(full=True)

            for img_index, xobject in enumerate(xobjects):
                x = xobject[0]
                image = doc.extract_image(x)
                image_data = image["image"]

                image_filename = (
                    f"{output_folder}/page{page_num + 1}_img{img_index + 1}.jpg"
                )
                with open(image_filename, "wb") as img_file:
                    img_file.write(image_data)

                # Apply image filter (Gaussian blur) to enhance clarity
                with Image.open(image_filename) as img:
                    img = img.convert("RGB")
                    img = img.filter(ImageFilter.GaussianBlur(radius=1))
                    img.save(image_filename)

        # Close the PDF document
        doc.close()

        return jsonify({"text": extracted_text, "images_folder": output_folder})


if __name__ == "__main__":
    os.makedirs("result/uploads", exist_ok=True)
    app.run(debug=True)
