import os
import fitz  # PyMuPDF
from PIL import Image, ImageFilter
from flask import Flask, render_template, request, jsonify,url_for
app = Flask(__name__)

# Set the template folder

app = Flask(__name__, template_folder="D:/Final project report/final project/project code/1_Language Translator/templates")



@app.route("/")
def homepage():
    return render_template("Homepage.html")


@app.route("/page1")
def page1():
    return render_template("Language_Translator.html")


@app.route("/page2")
def page2():
    return render_template("Drag_Drop.html")

@app.route("/page3")
def page3():
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

        return render_template("result.html", extracted_text=extracted_text, images_folder=output_folder, os=os)



@app.route("/page4")
def page4():
    return render_template("Text_To_Speech.html")


@app.route("/page5")
def page5():
    return render_template("Dictionary.html")


@app.route("/page6")
def page6():
    return render_template("File_Foramat.html")


@app.route("/page7")
def page7():
    return render_template("Palindrome.html")


@app.route("/page8")
def page8():
    return render_template("Notes.html")


@app.route("/page9")
def page9():
    return render_template("Quote_Generator.html")


#    GAMES SECTION STARTS FROM HERE
@app.route("/page10")
def page10():
    return render_template("Word_Guessing_Game.html")


@app.route("/page11")
def page11():
    return render_template("Word_Scramble_Game.html")


@app.route("/page12")
def page12():
    return render_template("Typing_Speed.html")


@app.route("/page13")
def page13():
    return render_template("Hangman_game.html")


@app.route("/page14")
def page14():
    return render_template("Quiz.html")


@app.route("/page15")
def page15():
    return render_template("Drawing.html")


if __name__ == "__main__":
    os.makedirs("result/uploads", exist_ok=True)
    app.run(debug=True)