#Blood_Cell_Detect

This is a demo project to elaborate a Deep Learning Models detecting and classifying blood cell images, the model is deployed on production using Flask API

Prerequisites

You must have yolov3,open cv and Flask (for API) installed.

Project Structure

This project has four major parts : 
.weights- This contains trained weight for the deep learning model 
app.py - This contains Flask APIs that receives users input through GUI or API calls, computes the precited value based on our model and returns it. 
templates - This folder contains the HTML template to allow user to enter health details and displays the predicted probability of having a cardiovascular disease.

Training the project

Training for this model was done on google colab using the free provided gpu, at the end of the taring a weight file is created 
-yolov3-custom_last.weight 

Run app.py using below command to start Flask API python app.py By default, flask will run on port 5000.

Navigate to URL http://localhost:5000 You should be able to view the homepage as below

Enter valid image and hit Predict.

If everything goes well, you should be able to see the predcited vaule on the HTML page! 
