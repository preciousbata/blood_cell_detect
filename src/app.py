# import the necessary packages
import numpy as np
from train import *
import cv2
import os
from flask import Flask, request, Response, jsonify, render_template
import logging
import io
import json
from PIL import Image


# paths

Lables = get_labels(labelsPath)
CFG = get_config(cfgpath)
Weights = get_weights(wpath)
nets = load_model(CFG, Weights)
Colors = get_colors(Lables)

# Step 2: Preparing Logging
logging.basicConfig(filename=r'C:\Users\Dell\Documents\GitHub\blood_cell_detect\Logs\response.logs',
                    level=logging.DEBUG,
                    filemode='w',
                    format='%(asctime)s %(levelname)s %(name)s  %(message)s')
logger = logging.getLogger()

# Initialize the Flask application
app = Flask(__name__, template_folder=r'C:\Users\Dell\Documents\GitHub\blood_cell_detect\template',
            static_folder=r'C:\Users\Dell\Documents\GitHub\blood_cell_detect\static')
port = int(os.environ.get('PORT', 5000))

@app.route('/', methods=['POST','GET'])
def home():
    return render_template('index.html')

# route http posts to this method
@app.route('/predict', methods=['POST','GET'])
def upload_predict():
    try:
        if request.method == 'POST':
            img = request.files["image"].read()
            img = Image.open(io.BytesIO(img))
            npimg = np.array(img)
            image = npimg.copy()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            res = get_prediction(image, nets, Lables, Colors)
        # image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        # show the output image
        # cv2.imshow("Image", res)
        # cv2.waitKey()
            image = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
            np_img = Image.fromarray(image)
            img_encoded = image_to_byte_array(np_img)
            return Response(response=img_encoded, status=200, mimetype="image/jpeg")
        return render_template('index.html')
    except TypeError:
        print('Invalid File type')



#Test on file upload from local machine
# def main():
#     # load our input image and grab its spatial dimensions
#     image = cv2.imread("./BloodImage_00000.jpg")
#     res = get_prediction(image, nets, Lables, Colors)
#     # image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#     # show the output image
#     cv2.imshow("Image", res)
#     cv2.waitKey()

# run from local machijne
# start flask app
# if __name__ == '__main__':
#     main()

# running in html
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
