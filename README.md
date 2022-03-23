# Blood_Cell_Detect

## Project Overview

This is a project to elaborate a Deep Learning Models localizing and classifying differnt types of blood cell in an image. The model is deployed on Azure using Flask 
  * Deployed on Azure: [Project link]()
  
## Technologies Used 
  * Python as the programming language
  * YOLOV3 for deep learning taining
  * Azure for cloud deployment

## Prerequisites

Install the latest version of YOLOV3, openCV and your favourite IDE.

## Project Structure

This project has essential folders such as:
  * Template: This folder contains the HTML template  which serves as the front end for user interface.
  * Input: Contains YOLO weight and configurations
  * src: This folder contains source codes such as config.py, app.py, model.py
  * Static: This folder contain css files, javascript files, images
 
## Running the Project
  1. Open the command prompt and navigate to project directory
  2. Install the necessary libraries and packages in the requirements file using the command----------> **pip -r requirements.txt**
  3. Change directory from the **root** folder into **src** folder by using the command---------------> **cd src**
  4. Once in the src folder, Run the command **python app.py**. The app will be hosted on your local machine on the default port 5000.
  5. Click on the link to 'http://localhost:5000' to access the web page
  6. Upload Valid Blood Sample image and click predict.
  7. If successful, a respose will be displayed on the browser

## Helpful Links
  * [YOLOV3 INSTALLATION]()
