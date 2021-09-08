# Blood_Cell_Detect

This is a project to elaborate a Deep Learning Models localizing and classifying differnt types of blood cell in a image, the model is deployed using Flask API

Prerequisites

You must have yolov3,open cv and Flask (for API) installed.

Project Structure

This project has major folders namely :

1.  src - which contain all the source code ( i.e app.py, config.py, train.py)

2.  template -  which contain HTML template frontend for the web app

3.  inputs -  contain the YOLOv3 weight and configuaration

RUNNING THE APP

1.  Run app.py using the command on your terminal to start Flask API, python app.py 
By default, flask will run on port 5000.

2.  Navigate to URL http://localhost:5000 You should be able to view the homepage as below

3.  Enter valid image and hit Predict.

If everything goes well, you should be able to see the predicted image on the HTML page! 
