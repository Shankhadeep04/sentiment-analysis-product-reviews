import streamlit as st
import joblib
import os

from src.data_preprocessing import clean_text


# Page configuration
st.set_page_config(
    page_title="Product Review Sentiment Analysis",
    page_icon="⭐",
    layout="wide"
)

# Load trained models
@st.cache_resource
def load_models():

    logistic_model = joblib.load(
        "models/logistic_model.pkl"
    )

    naive_bayes_model = joblib.load(
        "models/naive_bayes_model.pkl"
    )

    return logistic_model, naive_bayes_model


# Load models
try:
    logistic_model, naive_bayes_model = load_models()

except FileNotFoundError:
    st.error("Model files not found. Please run py main.py first.")
    st.stop()


# Application title
st.title("⭐ Product Review Sentiment Analysis")

st.write(
    "Analyze customer product reviews using Natural Language Processing "
    "and Machine Learning."
)

st.divider()


# Sidebar
st.sidebar.title("Project Information")

st.sidebar.write("Machine Learning Algorithms:")

st.sidebar.write("1. Logistic Regression")
st.sidebar.write("2. Naive Bayes")

st.sidebar.write("NLP Technique: TF-IDF")


# Model selection
model_choice = st.selectbox(
    "Select Machine Learning Model",
    ["Logistic Regression", "Naive Bayes"]
)

# Review input
review = st.text_area(
    "Enter Your Product Review",
    placeholder="Example: Excellent product with amazing quality..."
)


# Prediction button
if st.button("Analyze Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a product review.")

    else:

        cleaned_review = clean_text(review)

        if not cleaned_review.strip():
            st.warning("Please enter a meaningful text review.")

        else:
            if model_choice == "Logistic Regression":
                model = logistic_model

            else:
                model = naive_bayes_model

            prediction = model.predict([cleaned_review])[0]

            probabilities = model.predict_proba(
                [cleaned_review]
            )[0]

            confidence = max(probabilities) * 100

            st.subheader("Sentiment Prediction")

            if prediction == "Positive":
                st.success("Positive Sentiment 😊")

            elif prediction == "Negative":
                st.error("Negative Sentiment 😞")

            else:
                st.info("Neutral Sentiment 😐")

            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

            st.write("### Sentiment Probabilities")

            for sentiment, probability in zip(
                model.classes_,
                probabilities
            ):

                st.write(
                    f"{sentiment}: {probability * 100:.2f}%"
                )

                st.progress(float(probability))


st.divider()

st.caption(
    "Developed using Python, NLP, TF-IDF and Machine Learning."
) is this ok
