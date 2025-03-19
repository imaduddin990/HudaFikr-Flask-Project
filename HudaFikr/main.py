import pandas as pd

# Add error handling for CSV file
try:
    # Read CSV file
    df = pd.read_csv("tafsiran.csv")
except FileNotFoundError:
    print("Error: tafsiran.csv file not found!")
    exit(1)

# Clean up columns for case-insensitive comparison
df["emotion_bm"] = df["emotion_bm"].astype(str).str.strip().str.lower()
df["emotion_en"] = df["emotion_en"].astype(str).str.strip().str.lower()

# Debug: Check the data loaded from CSV
print(df.head())

# Ask user for language preference
language = input("Pilih bahasa (BM/EN): ").strip().lower()

# Validate language input
if language not in ["bm", "en"]:
    print("Pilihan bahasa tidak sah. Default ke BM.")
    language = "bm"

while True:
    # Ask for emotion in selected language
    if language == "bm":
        emotion = input("Masukkan emosi anda: ").strip().lower()
        result = df[df["emotion_bm"] == emotion]
        if not result.empty:
            print(f"\nSurah: {result.iloc[0]['surah']} Ayat {result.iloc[0]['ayat']}")
            print(f"Ayat: {result.iloc[0]['tafsiran_bm']}")
            break
        else:
            print("Maaf, emosi ini tiada dalam senarai. Sila cuba lagi.")
    else:
        emotion = input("Enter your emotion: ").strip().lower()
        result = df[df["emotion_en"] == emotion]
        if not result.empty:
            print(f"\nSurah: {result.iloc[0]['surah']} Verse {result.iloc[0]['ayat']}")
            print(f"Translation: {result.iloc[0]['tafsiran_en']}")
            break
        else:
            print("Sorry, this emotion is not in the list. Please try again.")