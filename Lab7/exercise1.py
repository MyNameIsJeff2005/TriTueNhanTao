import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Naive Bayes Text Classifier",
    page_icon="🔮",
    layout="wide"
)

st.markdown("""
<style>
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    data = pd.read_csv('Education.csv')
    return data

@st.cache_data
def split_train_test(data, ratio_test=0.2):
    np.random.seed(42)
    index_permu = np.random.permutation(len(data))
    data_permu = data.iloc[index_permu]
    test_size = int(len(data_permu) * ratio_test)
    train_set = data_permu.iloc[:-test_size]
    test_set = data_permu.iloc[-test_size:]
    return train_set.reset_index(drop=True), test_set.reset_index(drop=True)

@st.cache_resource
def train_models():
    data = load_data()
    train_set, test_set = split_train_test(data)
    X_train, y_train = train_set['Text'], train_set['Label']
    y_train_numeric = y_train.map({"positive": 1, "negative": 0})

    bernoulli_vec = CountVectorizer(binary=True, stop_words='english')
    X_train_bernoulli = bernoulli_vec.fit_transform(X_train)
    bernoulli_model = BernoulliNB()
    bernoulli_model.fit(X_train_bernoulli, y_train_numeric)

    multinomial_vec = CountVectorizer(stop_words='english')
    X_train_multinomial = multinomial_vec.fit_transform(X_train)
    multinomial_model = MultinomialNB()
    multinomial_model.fit(X_train_multinomial, y_train_numeric)

    return bernoulli_model, bernoulli_vec, multinomial_model, multinomial_vec

def main():
    st.title("🔮 Naive Bayes Text Classification")
    st.markdown("Enter text to classify as **positive** or **negative** educational content.")
    st.markdown("---")

    bernoulli_model, bernoulli_vec, multinomial_model, multinomial_vec = train_models()

    if 'user_text' not in st.session_state:
        st.session_state['user_text'] = ""

    user_text = st.text_area(
        "Enter text to classify:",
        placeholder="Type your educational text here...",
        height=100,
        value=st.session_state['user_text']
    )

    submit_button = st.button("🚀 Classify Text", type="primary", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sample: Positive Text"):
            st.session_state['user_text'] = "This course provides excellent learning opportunities and valuable knowledge."
    with col2:
        if st.button("Sample: Negative Text"):
            st.session_state['user_text'] = "The educational program was poorly designed and not helpful."

    if user_text and submit_button:
        user_text_bernoulli = bernoulli_vec.transform([user_text])
        user_text_multinomial = multinomial_vec.transform([user_text])

        bernoulli_pred_user = bernoulli_model.predict(user_text_bernoulli)[0]
        bernoulli_proba_user = bernoulli_model.predict_proba(user_text_bernoulli)[0]

        multinomial_pred_user = multinomial_model.predict(user_text_multinomial)[0]
        multinomial_proba_user = multinomial_model.predict_proba(user_text_multinomial)[0]

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🎯 Bernoulli Naive Bayes")
            pred_label = "Positive" if bernoulli_pred_user == 1 else "Negative"
            confidence = max(bernoulli_proba_user)
            st.success(f"**Prediction:** {pred_label}") if pred_label == "Positive" else st.error(f"**Prediction:** {pred_label}")
            st.info(f"**Confidence:** {confidence:.3f}")

            prob_df = pd.DataFrame({'Class': ['Negative', 'Positive'], 'Probability': bernoulli_proba_user})
            fig_prob = px.bar(prob_df, x='Class', y='Probability', title="Class Probabilities - Bernoulli",
                              color='Class', color_discrete_map={'Negative': 'red', 'Positive': 'green'})
            st.plotly_chart(fig_prob, use_container_width=True)

        with col2:
            st.markdown("### 📊 Multinomial Naive Bayes")
            pred_label = "Positive" if multinomial_pred_user == 1 else "Negative"
            confidence = max(multinomial_proba_user)
            st.success(f"**Prediction:** {pred_label}") if pred_label == "Positive" else st.error(f"**Prediction:** {pred_label}")
            st.info(f"**Confidence:** {confidence:.3f}")

            prob_df = pd.DataFrame({'Class': ['Negative', 'Positive'], 'Probability': multinomial_proba_user})
            fig_prob = px.bar(prob_df, x='Class', y='Probability', title="Class Probabilities - Multinomial",
                              color='Class', color_discrete_map={'Negative': 'red', 'Positive': 'green'})
            st.plotly_chart(fig_prob, use_container_width=True)

        st.markdown("---")
        st.markdown("### 📈 Model Comparison")
        comparison_df = pd.DataFrame({
            'Model': ['Bernoulli NB', 'Multinomial NB'],
            'Prediction': [
                "Positive" if bernoulli_pred_user == 1 else "Negative",
                "Positive" if multinomial_pred_user == 1 else "Negative"
            ],
            'Confidence': [max(bernoulli_proba_user), max(multinomial_proba_user)]
        })
        st.dataframe(comparison_df, use_container_width=True)

        if comparison_df['Prediction'].iloc[0] == comparison_df['Prediction'].iloc[1]:
            st.success("✅ Both models agree on the prediction!")
        else:
            st.warning("⚠️ Models have different predictions - consider the confidence scores.")

main()
