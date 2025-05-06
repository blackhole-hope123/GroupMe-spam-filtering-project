import json
import os
RAW_DATA_FOLDER="data"
CLEAN_DATA_FOLDER="clean_data"
RAW_DATA_FILE="message.json"
CLEAN_DATA_FILE="cleaned_message.json"

def load_data(data_dir):
    folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]
    if not os.path.exists(CLEAN_DATA_FOLDER):
        os.makedirs(CLEAN_DATA_FOLDER)
    output_folder=CLEAN_DATA_FOLDER
    for folder in folders:
        folder_path=os.path.join(data_dir,folder)
        for file in os.listdir(folder_path):
            if file==RAW_DATA_FILE:    
                file_path=os.path.join(folder_path,RAW_DATA_FILE)
                # Open and load the JSON file
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                messages=[]
                for message in data:
                    if "text" in message and message["text"]!=None and "system" in message and not message["system"]:
                        messages.append(message["text"])
                output_subfolder=os.path.join(output_folder,folder)
                if not os.path.exists(output_subfolder):
                    os.makedirs(output_subfolder)
                output_path=os.path.join(output_subfolder,CLEAN_DATA_FILE)
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(messages, f, indent=2)
                break
    return

load_data(RAW_DATA_FOLDER)