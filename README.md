# Language Identification Model

## Overview
This project is a **Language Identification Model** that supports **21 languages**. Users can input text in any of these languages, and the model will predict which language it belongs to.

Additionally, a **Streamlit application** has been developed and deployed on **Streamlit Cloud**, providing a user-friendly interface for testing the model.

## Features
- Supports **21 languages**
- Accepts user input and predicts the language
- Built with **Machine Learning/NLP** techniques
- **Streamlit-based** web application for easy interaction
- Deployed on **Streamlit Cloud** for online access

## Installation
To run the model locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone <repo_link>
   cd <repo_directory>
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

## Usage
1. Open the Streamlit web application.
2. Enter text in any of the 21 supported languages.
3. Click the "Predict" button.
4. The model will display the predicted language.

## Deployment
The application is deployed on **Streamlit Cloud**. You can access it here: [language-identification-model](<https://language-identification-model.streamlit.app/>)

## Technologies Used
- Python
- Streamlit
- Scikit-learn / Any other ML library used
- NLP techniques for language detection
