import os
from flask import Flask, request, render_template, send_from_directory,flash
from PIL import Image
from pylab import *
from tensorflow.keras.models import load_model

app=Flask(__name__)
app.secret_key='random string'

classes=['Apple','Corn','Grape','Peach','Tomato']

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/upload")
# def upload():
#     return render_template("upload.html")
@app.route("/upload")
def upload():
    return render_template("upload.html")
@app.route('/upload1/<filename>')
def send_image(filename):
    print('Plant_Result')
    return send_from_directory("images", filename)

@app.route("/upload1", methods=["POST","GET"])
def upload1():
    print('a')
    if request.method=='POST':
        myfile = request.files['file']
        print("Image_uploaded")
        fn = myfile.filename
        mypath = os.path.join('images/', fn)
        myfile.save(mypath)

        print("{} is the file name", fn)
        print("Accept incoming file:", fn)
        print("Save it to:", mypath)
        # import tensorflow as tf
        import numpy as np
        from tensorflow.keras.preprocessing import image
        from tensorflow.keras.models import load_model
        
        new_model = load_model("visualizations/model_1.h5")
        test_image = image.load_img(mypath, target_size=(64,64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)

        prediction = classes[np.argmax(result)]
    return render_template("template.html", image_name=fn, text=prediction)




if __name__=='__main__':
    app.run(debug=True)