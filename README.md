# HudaFikr - Quranic Verses Based on Emotions

HudaFikr is a simple Flask-based web application that suggests Quranic verses based on the user's emotions. Users can enter an emotion in either Malay or English, and the application will provide a relevant verse along with its interpretation in the appropriate language.

## Features
- Supports both Malay and English input.
- Displays a relevant Quranic verse and its interpretation.
- Simple and lightweight web interface using Flask.
- Handles errors such as missing CSV files.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3
- Flask
- Pandas
- A CSV file (`tafsiran.csv`) containing Quranic verses linked to emotions.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/hudafikr.git
   cd hudafikr
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000/`.

## File Structure
```
HudaFikr/
│-- app.py          # Main Flask application
│-- main.py         # Standalone script for CLI-based interaction
│-- templates/
│   └── index.html  # HTML template for the web interface
│-- tafsiran.csv    # CSV file containing Quranic verses and emotions
│-- static/         # (Optional) Folder for static files like CSS/JS
│-- requirements.txt  # Dependencies list
```

## Usage
- Enter an emotion (Malay or English) into the input box.
- The app will find and display a relevant Quranic verse along with its interpretation.
- If no matching verse is found, a message will be displayed.

## CSV Format
Ensure that `tafsiran.csv` follows this format:
```
emotion_bm,emotion_en,surah,ayat,tafsiran_bm,tafsiran_en
sedih,sad,2,286,"Janganlah kamu bersedih, sesungguhnya Allah bersama kita.","Do not be sad, indeed Allah is with us."
```

## Contributions
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.
