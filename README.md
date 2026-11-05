# Product Review Sentiment Analysis

A Streamlit web app that predicts product-review sentiment using a trained
Logistic Regression model and TF-IDF vectorizer.

## Features
- Enter a product review and get a sentiment prediction.
- View prediction probabilities.
- Uses the trained model and vectorizer included in this repository.

## Project files
```text
product-review-sentiment-streamlit/
├── app.py
├── sentiment_model.pkl
├── vectorizer.pkl
└── requirements.txt
```

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Upload these files to the root of a GitHub repository.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Select **Create app** and choose your repository and branch.
4. Set the main file path to `app.py`.
5. Select **Deploy**.

## Important model note
The supplied model has two output classes (0 and 1). This app maps them to
Negative and Positive, respectively, based on the labeling convention in the
project notebook. It does not currently provide a Neutral prediction.
