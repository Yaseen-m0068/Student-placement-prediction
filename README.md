# Placement Prediction App

This project is a simple Streamlit web app that predicts whether a student is likely to get placed based on academic and skill-related inputs.

## What it does

The app uses a logistic regression model trained on student placement data and asks for inputs such as:

- CGPA
- IQ
- Communication skills
- Technical skills
- Internships
- Projects
- Extracurricular activity level
- Department

It then shows whether the student is likely to be placed or not.

## Run locally

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

   pip install -r requirements.txt
   
3. Start the app:

   streamlit run app.py

4. Open the local URL shown in the terminal in your browser.

## Project files

- `app.py` – Streamlit interface and prediction logic
- `placement_data.csv` – dataset used for model training
- `placement_prediction.ipynb` – notebook for analysis and model development
- `requirements.txt` – Python dependencies

## Tech stack

- Python
- Streamlit
- scikit-learn
- pandas
- NumPy
- joblib
