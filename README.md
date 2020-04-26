# Reddit-Flair-Detection

### Note: I triend to use Heroku but it only allows data upto 500MB. Because of the Machine and Deep learning Libraries my data became 540MB (only tensorflow library was of 430MB) So I didnt hosted this on Heroku please check the whole README.md file and Evaluate the project. Please dont let my Hard work get wasted. 

### Highlights: I got 94.2% validation accuracy and 0.16 validation loss on my dataset. Used ***Deep and Transfer Learning*** to make the model. Here is a Screesnhot of my data flow of my Neural Network.
![index](https://user-images.githubusercontent.com/41755284/80312606-9e47b380-8803-11ea-84ac-c9dc5dce7e0f.png)

### Open the notebook in Google Colab (All of the libraries would be available there). Link to colab is given inside the notebook.

### Before opening the notebook, please go through the following steps:
Create your reddit application first from <a href="https://www.reddit.com/prefs/apps">here</a>
![](https://miro.medium.com/max/1280/1*GQ8IREDENnkCRQT3VS55mQ.png)
![](https://miro.medium.com/max/1280/1*ssLYczSLGzfm6SPM7mWzBg.png)
![](https://miro.medium.com/max/1280/1*khszOCCaCtqZ6jM19uhpiQ.png)

### I also used pre-trained embedding matrix that I downoaded from kaggle in the notebook. Please Go through the following steps.
- Make an account on Kaggle
- Get your kaggle.json file from their.
- Paste the kaggle username and key in the file when needed.
- Open the notebook on Google Colab.

### Install Required Library
requirements.txt file is avilable inside the project's folder
- pip install -r requirement.txt

### Web Application
Write your reddit credentials in views.py file inside Flare_Detector_app folder<br>
Execute following command-
- cd Flare_Detector
- python manage.py runserver<br>
Then open url http://127.0.0.0:8000 on your browser.

### RESTful API
Use Post request with url http://127.0.0.0:8000/file/upload/<br>
Use a text file to upload with key=files
Use Postman to check the API.

### Screenshots of Web Application
![Screenshot (563)](https://user-images.githubusercontent.com/41755284/80311395-1199f700-87fd-11ea-8b07-ac606a54f90f.png)


