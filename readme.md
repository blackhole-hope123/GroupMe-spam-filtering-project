# Project: GroupMe spam filtering API

## Description

This part of the project is aimed at wrapping the model into a flask app and deploy it on the Microsoft Azure portal. THe main file here is app.py, which designs the frontend webpage and also its function to get and post, maing the app interative.


## Project Structure Overview

```

├── ML model/                           # folder containing files on how the model is trained and evaluated, including how data is collected and labelled, which has a readme.md for itself.
├── app.py                              # python file designing the flask app
├── requirements.txt                    # text file containing all the required python modules
├── test.py                             # a test file to test the how well the app runs (after the human verification)
└── readme.md                           # This file
```

### Deployed App

The deploye app is available on https://spam-filtering-app-hvb4e5fedkfjahf0.eastus-01.azurewebsites.net/ .
