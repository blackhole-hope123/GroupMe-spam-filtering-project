# Backend: the backend model construction

## Description

This part of the project designs a machine learning model to filter spam messages in GroupMe chats, where it used supervised learning, or more specifically the linear support vector machine algorithm. There are several steps in the constructing the model, first, one collects the data from GroupMe, and then one keeps only the relevant chat messages for analysis. Using a set of criteria, these messages are labelled by an algorithm as "spam" or "ham" (not spam). A refining process follows, where a streamlit app is designed so that one can refine the label, to ensure that the data is properly annotated. Finally, the model is train and evaluated on this data set.


## Project Structure Overview

```
ML model/
├── data/                                       # storing the original data
├── clean_data/                                 # storing only the messages by human in the GroupMe chats
├── labelled_data/                              # storing the labelled data (by a fixed set of rules)
├── refined_labels/                             # storing the refined labelled data (after the human verification)
├── data_labelling.py                           # python file to label the data by a fixed set of rules
├── data_loading.py                             # python file to load the data from the original data downloaded from GroupMe
├── label_refining_streamlit_app.py             # streamlit app for human annotator to refine the labels
├── model_training_and_evaluation.py            # python file to train and evaluate the (linear SVM) model
├── spam_model.pkl                              # file recording parameters of the model
└── README.md                                   # This file
```

### Example Usage

## Setup Instructions

1. Clone this repository
```bash
git clone https://github.com/blackhole-hope123/GroupMe-spam-filtering-project.git
cd C:\Users\your-username\GroupMe-spam-filtering-project
```

2. Install the packages
```bash
pip install -r requirements.txt
```

#### Running Scripts
for example, to run the model training and evaluation script:
```bash
cd "ML model"
python model_training_and_evaluation.py 
```

## Acknowledgement 
The dataset is from my own GroupMe chats.
