# Blood_Cell_Detect

## Project Overview

This is a project to showcase a Deep Learning Model localizing and classifying different types of blood cells from an image from an electronic microscope.
  
## Technologies Used 
  * Python as the programming language
  * YOLOV3 for deep learning training

## Prerequisites

Install the latest version of YOLOV3, openCV and your favourite IDE.

## Project Structure

This project has essential folders such as:
  * Template: This folder contains the HTML template  which serves as the front end for user interface.
  * Input: Contains YOLO weight and configurations
  * src: This folder contains source codes such as config.py, app.py, model.py
  * Static: This folder contains CSS files, javascript files, images
 
## Running the Project
  1. Open the command prompt and navigate to the project directory
  2. Install the necessary libraries and packages in the requirements file using the command----------> **pip  install -r requirements.txt**
  3. Change directory from the **root** folder into **src** folder by using the command---------------> **cd src**
  4. Once in the src folder, Run the command **python app.py**. The app will be hosted on your local machine on the default port 5000.
  5. Click on the link to 'http://localhost:5000' to access the web page
  6. Upload the Valid Blood Sample image and click predict.
  7. If successful, a response will be displayed on the browser
## Screenshot
[![Screenshot-14.png](https://i.postimg.cc/ZqcCk0yb/Screenshot-14.png)](https://postimg.cc/jWDsPxXm)

## Helpful Links
  * [YOLOV3 INSTALLATION]()
