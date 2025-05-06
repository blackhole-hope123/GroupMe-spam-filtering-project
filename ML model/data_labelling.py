import json
import re
import os
from textblob import TextBlob


PRELABELLED_DATA_FOLDER=os.path.join("ML model", "prelabelled_data")
CLEAN_DATA_FOLDER=os.path.join("ML model", "clean_data")
PRELABELLED_DATA_FILE="labelled_message.json"
CLEAN_DATA_FILE="cleaned_message.json"

spam_keywords = ["ticket", "tickets", "limited time", "claim now"]
spam_patterns = [
    r"sell.*ticket.*"
]
nonspam_patterns = [
    r"do\s+not|don't.*sell.*ticket.*"
]

def annotate_data(data_dir):
    folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]
    if not os.path.exists(PRELABELLED_DATA_FOLDER):
        os.makedirs(PRELABELLED_DATA_FOLDER)
    output_folder=PRELABELLED_DATA_FOLDER
    for folder in folders:
        folder_path=os.path.join(data_dir,folder)
        if CLEAN_DATA_FILE in os.listdir(folder_path):
            labelled_data=[]
            file_path=os.path.join(folder_path,CLEAN_DATA_FILE)
            with open(file_path, 'r', encoding='utf-8') as f:
                clean_messages = json.load(f)
            for message in clean_messages:
                message_with_label={}
                message_with_label["message"]=message
                message_with_label["prelabel"]=is_spam(message)
                labelled_data.append(message_with_label)
            output_subfolder=os.path.join(output_folder,folder)
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            output_path=os.path.join(output_subfolder,PRELABELLED_DATA_FILE)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(labelled_data, f, indent=2)
        else:
            raise Exception("There is no message.json file")
    return

            
# load_data


def is_spam(msg):
    msg_lower = msg.lower()
    nonspam_pattern_match = any(re.search(pattern, msg_lower) for pattern in nonspam_patterns)
    if nonspam_pattern_match:
        return "ham"
    
    keyword_match = any(kw in msg_lower for kw in spam_keywords)
    pattern_match = any(re.search(pattern, msg_lower) for pattern in spam_patterns)
    sentiment_score = TextBlob(msg).sentiment.polarity
    overly_positive = sentiment_score > 0.8
    
    if keyword_match + pattern_match + overly_positive >= 1:
        return "spam"
    return "ham"

annotate_data("clean_data")
