import joblib
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import json
import pandas as pd
import os

def main():
    df = pd.DataFrame()
    DATA_FOLDER="refined_labels"
    DATA_FILE="final_labels.json"
    subfolders=[f for f in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, f))]
    for subfolder in subfolders:
        subfolder_path=os.path.join(DATA_FOLDER,subfolder)
        data_file_path=os.path.join(subfolder_path,DATA_FILE)
        with open(data_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        df = pd.concat([pd.DataFrame(data),df],axis=0)

    # clean data
    df = df[df["label"] != "skip"]
    df = df[["message", "label"]]
    df["label"] = df["label"].map({"spam": 1, "ham": 0})


    X = df["message"]
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = make_pipeline(
        CountVectorizer(stop_words="english", max_features=1000),
        LinearSVC()
    )
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    print("SVM", classification_report(y_test, y_pred))
    joblib.dump(pipeline, "spam_model.pkl")


if __name__=="__main__":
    main()