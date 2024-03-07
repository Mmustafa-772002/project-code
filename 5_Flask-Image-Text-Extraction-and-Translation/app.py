import easyocr
import translators as tss
from flask import Flask, render_template, Response, request
import os
import cv2
from PIL.Image import Resampling


tnl=['en','en']
app = Flask(__name__)
path = os.getcwd()
image = None

lng = {  'Bengali': 'bn', 'English': 'en','Gujarati': 'gu', 'Hindi': 'hi', 'Kannada': 'kn','Malayalam': 'ml', 'Marathi': 'mr', 'Nepali': 'ne', 'Odia': 'or','Punjabi': 'pa', 'Tamil': 'ta', 'Telugu': 'te', 'Urdu': 'ur',
    }

def resu(file):
    global data
    reader = easyocr.Reader(['en'])
    result = reader.readtext(file)
    if len(result)<1:
        result= ["No data found"]
    data = [i[1] for i in result]
    return data

def ocr(val):
    # print(image)
    print(tnl)
    reader = easyocr.Reader([tnl[0]])
    result = reader.readtext(image)

    if len(result)<1:
        result= ["No data found"]
    data = [i[1] for i in result]

    txt=[]
    for bbox, text, prob in result:
        # Get the coordinates of the bounding box
        xmin, ymin = [int(coord) for coord in bbox[0]]
        xmax, ymax = [int(coord) for coord in bbox[2]]
        # print(text)
        # Draw the bounding box and the text on the image
        if val==0:
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
            cv2.putText(image, text, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            txt.append(text)
        else:
            text = tss.google(text, tnl[0],tnl[1])
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
            cv2.putText(image, text, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (2, 255, 100), 1)
            txt.append(text)
    return txt

def image_process(image):
    ret, jpeg = cv2.imencode('.jpg', image)
    frame = jpeg.tobytes()
    yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/image_filters/img_share')
def img_share():
    global image
    # image=cv2.resize(image, (480, 480))
    return Response(image_process(image), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/trans/', methods=['POST'])
def trans():
    if request.method == "POST":
        value = request.form.get("value")
        if value!=tnl[1]:
            tnl[1]=value
            for i in range(len(data)):
                data[i]=tss.google(data[i], tnl[0], tnl[1])
    return render_template('result.html',data=data)


@app.route('/')
def home():
    return render_template('image.html',lng=lng.keys())

@app.route('/upload', methods=['POST'])
def drop_image():
    if request.method == 'POST':
        file = request.files['image']
        path = file.filename
        print(1)
        file.save(path)
        data = ocr(0)
        return render_template('result.html',data=data)
    
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           

    
@app.route('/image_upload/',methods=['POST','GET'])
def img_():
    global image
    if request.method == 'POST':
        dropdown_value1 = request.form.get("from")
        dropdown_value2 = request.form.get("to")

        tnl[0]=lng[dropdown_value1]
        tnl[1]=lng[dropdown_value2]
        
        if tnl[1] != tnl[0]:
            flag = 1

        f = request.files['image']
        path = f.filename
        f.save(path)
        image = cv2.imread(path)
        data=ocr(flag)
        return render_template('result.html',data=data)

# Back button route
@app.route('/go_back')
def go_back():
    # Use the url_for function to get the URL for the 'index' endpoint
    return redirect(url_for('index'))

# Redirect to the "image.html" page on button click
@app.route('/redirect_to_image')
def redirect_to_image():
    return redirect(url_for('image_page'))


if __name__ == '__main__':
   app.run(debug=True)
