import streamlit as st
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Product Review Sentiment Analysis",
    page_icon="⭐",
    layout="centered"
)

@st.cache_resource
def load_artifacts():
    model = joblib.load(BASE_DIR / "sentiment_model.pkl")
    vectorizer = joblib.load(BASE_DIR / "vectorizer.pkl")
    return model, vectorizer

st.title("⭐ Product Review Sentiment Analysis")
st.write(
    "Enter a product review to predict whether its sentiment is "
    "positive or negative using a trained Logistic Regression model."
)

try:
    model, vectorizer = load_artifacts()
except Exception as exc:
    st.error("The model files could not be loaded. Make sure both "
             "`sentiment_model.pkl` and `vectorizer.pkl` are in the app folder.")
    st.exception(exc)
    st.stop()

review = st.text_area(
    "Enter your product review",
    placeholder="Example: The product quality is excellent and delivery was fast...",
    height=140
)

if st.button("Analyze Sentiment", type="primary", use_container_width=True):
    if not review.strip():
        st.warning("Please enter a review first.")
    else:
        try:
            review_vector = vectorizer.transform([review.strip()])
            prediction = model.predict(review_vector)[0]

            # The uploaded model contains two classes: 0 and 1.
            # The project notebook defines negative as 0 and positive as 1.
            labels = {0: "Negative", 1: "Positive"}
            sentiment = labels.get(prediction, str(prediction))

            st.subheader("Prediction")
            if sentiment.lower() == "positive":
                st.success("Positive sentiment 😊")
            elif sentiment.lower() == "negative":
                st.error("Negative sentiment 😞")
            else:
                st.info(f"Predicted class: {sentiment}")

            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba(review_vector)[0]
                class_labels = [
                    labels.get(cls, str(cls)) for cls in model.classes_
                ]
                st.subheader("Prediction confidence")
                for label, probability in zip(class_labels, probabilities):
                    st.write(f"**{label}:** {probability * 100:.2f}%")
                    st.progress(float(probability))

        except Exception as exc:
            st.error("Prediction failed. Please check the model and vectorizer files.")
            st.exception(exc)

st.divider()
st.caption("Built with Python, Streamlit, TF-IDF and Logistic Regression.")
