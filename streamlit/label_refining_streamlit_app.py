import streamlit as st
import os
import json

INPUT_FOLDER=os.path.join("app","ML model","labelled_data")
OUTPUT_FOLDER=os.path.join("app","ML model","refined_labels")
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
st.title("📬 Message Labeling App")

folder = st.text_input("Enter group id:")

input_folder_path=os.path.join(INPUT_FOLDER,folder)
output_folder_path=os.path.join(OUTPUT_FOLDER,folder)
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)
if folder:
    try:
        files = os.listdir(input_folder_path)
        json_files = [f for f in files if f.endswith(".json")]

        for f in json_files:
            if f=="labelled_message.json":
                json_path = os.path.join(input_folder_path, f)
                with open(json_path, "r", encoding="utf-8") as f:
                    messages = json.load(f)

                st.success(f"Loaded {len(messages)} messages from {json_files[0]}.")

                if "index" not in st.session_state:
                    st.session_state.index = 0
                    st.session_state.labels = []

                idx = st.session_state.index

                if idx < len(messages):
                    current = messages[idx]
                    st.markdown(f"### Message {idx + 1}/{len(messages)}")
                    st.write(current["message"])
                    st.markdown(f"**Pre-label:** `{current.get('prelabel', 'unknown')}`")

                    label = st.radio("Your label:", ["spam", "ham", "skip"], horizontal=True)

                    if st.button("Next"):
                        st.session_state.labels.append({
                            "message": current["message"],
                            "prelabel": current.get("prelabel"),
                            "label": label
                        })
                        st.session_state.index += 1
                        st.experimental_rerun()
                else:
                    st.success("✅ All messages labeled.")
                    save_path = os.path.join(output_folder_path, "final_labels.json")
                    with open(save_path, "w", encoding="utf-8") as f:
                        json.dump(st.session_state.labels, f, indent=2, ensure_ascii=False)
                    st.write(f"Results saved to `{save_path}`")
                    st.button("Reset Session", on_click=lambda: st.session_state.clear())
            else:
                st.warning("No intended JSON files found in that folder.")
    except Exception as e:
        st.error(f"Error: {e}")
