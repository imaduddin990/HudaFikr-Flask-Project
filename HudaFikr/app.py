from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Add error handling for CSV file
try:
    df = pd.read_csv("tafsiran.csv")
except FileNotFoundError:
    print("Error: tafsiran.csv file not found!")
    df = pd.DataFrame()  # Create empty DataFrame to avoid errors

def get_ayat_by_emotion(emotion):
    if df.empty:
        return None, None, None, None
        
    # Check if the emotion matches Malay or English
    malay_match = df[df["emotion_bm"].str.lower() == emotion.lower()]
    english_match = df[df["emotion_en"].str.lower() == emotion.lower()]
    
    if not malay_match.empty:
        # If Malay input, return only Malay tafsiran
        row = malay_match.iloc[0]
        return row["surah"], row["ayat"], row["tafsiran_bm"], None
    elif not english_match.empty:
        # If English input, return only English tafsiran
        row = english_match.iloc[0]
        return row["surah"], row["ayat"], None, row["tafsiran_en"]
    
    return None, None, None, None

@app.route("/", methods=["GET", "POST"])
def index():
    ayat_data = None
    if request.method == "POST":
        emotion = request.form.get("emotion").strip().lower()
        print(f"Received emotion: {emotion}")  # Debugging log
        surah, ayat, tafsiran_bm, tafsiran_en = get_ayat_by_emotion(emotion)
        if surah:
            ayat_data = {
                "surah": surah,
                "ayat": ayat,
                "tafsiran_bm": tafsiran_bm,
                "tafsiran_en": tafsiran_en,
            }
        print(f"Ayat Data: {ayat_data}")  # Debugging log
    return render_template("index.html", ayat_data=ayat_data)

if __name__ == "__main__":
    app.run(debug=True)