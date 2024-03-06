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
        # Save the uploaded PDF file
        pdf_file_path = os.path.join("uploads", "uploaded.pdf")
        file.save(pdf_file_path)

        # Open the PDF file
        doc = fitz.open(pdf_file_path)

        # Extract text from the PDF
        extracted_text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            extracted_text += page.get_text("text")

        # Save the extracted text to a text file
        text_file_path = os.path.join("static", "extracted_text.txt")
        with open(text_file_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)

        # Create a folder to save the extracted images
        output_folder = 'static/extracted_images'
        os.makedirs(output_folder, exist_ok=True)

        # Extract images from the PDF
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            xobjects = page.get_images(full=True)

            for img_index, xobject in enumerate(xobjects):
                x = xobject[0]
                image = doc.extract_image(x)
                image_data = image['image']

                image_filename = f"{output_folder}/page{page_num + 1}_img{img_index + 1}.jpg"
                with open(image_filename, "wb") as img_file:
                    img_file.write(image_data)

                # Apply image filter (Gaussian blur) to enhance clarity
                with Image.open(image_filename) as img:
                    img = img.convert('RGB')
                    img = img.filter(ImageFilter.GaussianBlur(radius=1))
                    img.save(image_filename)

        # Close the PDF document
        doc.close()

        return jsonify({"text": extracted_text, "images_folder": output_folder})

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
