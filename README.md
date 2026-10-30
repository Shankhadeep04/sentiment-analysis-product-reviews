# Product Review Sentiment Analysis

## 📌 Project Overview

The goal of this project is to analyze customer reviews and determine their sentiment — **Positive, Negative, or Neutral** — based on the text content of reviews and associated metadata.

This project helps understand customer feedback, identify product strengths and weaknesses, and improve the overall customer experience through actionable insights.

If you find this project useful, please consider giving it a ⭐ on GitHub. Contributions are always welcome!

## 📸 Project Screenshot

![Project Screenshot](Screenshot%20(130).png)

## 📑 Table of Contents

- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLTK
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📂 Project Structure

```text
Product_Review_Sentiment_Analysis/
│
├── dataset/
│   └── product_reviews.csv
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── model_evaluation.py
│
├── models/
│   └── sentiment_model.pkl
│
├── app.py
├── requirements.txt
└── README.md

### Installation

To set up the project, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/Product-Review-Sentiment-Analysis.git

# Navigate into the project directory
cd Product-Review-Sentiment-Analysis

# Create a virtual environment
python -m venv Product_Review_Analysis

# Activate the virtual environment
# On Windows
Product_Review_Analysis\Scripts\activate
# On macOS/Linux
source Product_Review_Analysis/bin/activate

# Install dependencies
pip install -r requirements.txt
```
### Usage
After setting up the project, you can run the Streamlit app with the following command:
```bash
streamlit run app.py
```
This will launch the application in your web browser, where you can input reviews and visualise sentiment analysis results.

### Features
- Sentiment classification of reviews (positive, negative, neutral)
- Visualisation of sentiment distribution across different product categories
- Real-time sentiment prediction for user-input reviews
- Interactive dashboard for exploring customer feedback

### Contributing
Contributions are welcome! Please read the contributing guidelines for details on how to contribute.
```bash
- Fork the repository.
- Create a new feature branch (git checkout -b feature-name).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature-name).
- Open a pull request.
```
### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any inquiries or feedback please contact me at https://github.com/Shankhadeep04
