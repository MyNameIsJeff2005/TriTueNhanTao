import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from scipy.stats import skew
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Drug Classifier GaussianNB",
    page_icon="💊",
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
    return pd.read_csv('drug.csv')


@st.cache_resource
def train_model(apply_scaler=False):
    data = load_data()
    X = data.drop(['Drug'], axis=1)
    y = data['Drug'].map({"drugA": 1, "drugB": 2, "drugC": 3, "drugX": 4, "DrugY": 5})

    X = pd.get_dummies(X, dtype='int')

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    scaler = None
    num_cols = ['Age', 'Na_to_K']

    if apply_scaler:
        scaler = StandardScaler()
        X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
        X_test[num_cols] = scaler.transform(X_test[num_cols])

    model = GaussianNB()
    model.fit(X_train, y_train)

    return model, X_train, X_test, y_train, y_test, scaler, num_cols


def main():
    st.title("💊 Drug Type Classifier - Gaussian Naive Bayes")
    st.markdown("Predict drug type based on patient attributes using GaussianNB.")

    data = load_data()

    st.markdown("### 📊 Raw Data")
    st.dataframe(data.head())

    st.markdown("### 📈 Na_to_K Distribution")
    sk = skew(data['Na_to_K'])
    st.info(f"Skewness of Na_to_K: {sk:.3f}")
    fig = px.histogram(data, x='Na_to_K', nbins=30, marginal="box", title="Distribution of Na_to_K")
    st.plotly_chart(fig, use_container_width=True)

    apply_scaler = st.toggle("⚙️ Apply StandardScaler to numerical features", value=False)
    model, X_train, X_test, y_train, y_test, scaler, num_cols = train_model(apply_scaler)

    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)

    st.markdown("### ✅ Model Performance")
    st.text(classification_report(y_test, y_pred))

    mapp = {1: "drugA", 2: "drugB", 3: "drugC", 4: "drugX", 5: "DrugY"}

    result_df = pd.DataFrame({
        'Actual': [mapp[i] for i in y_test],
        'Predicted': [mapp[i] for i in y_pred]
    }).reset_index(drop=True)
    st.dataframe(result_df.head(10))

    st.markdown("---")
    st.markdown("## 🧪 Predict New Case")

    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = {}

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=35)
        sex = st.selectbox("Sex", ["F", "M"])
    with col2:
        bp = st.selectbox("BP", ["HIGH", "NORMAL", "LOW"])
        cholesterol = st.selectbox("Cholesterol", ["HIGH", "NORMAL"])
    with col3:
        na_to_k = st.number_input("Na_to_K", min_value=0.0, value=15.0)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sample 1"):
            st.session_state['user_input'] = {'Age': 25, 'Sex': 'F', 'BP': 'HIGH', 'Cholesterol': 'HIGH', 'Na_to_K': 30}
    with col2:
        if st.button("Sample 2"):
            st.session_state['user_input'] = {'Age': 60, 'Sex': 'M', 'BP': 'LOW', 'Cholesterol': 'NORMAL', 'Na_to_K': 10}

    if st.session_state['user_input']:
        age = st.session_state['user_input']['Age']
        sex = st.session_state['user_input']['Sex']
        bp = st.session_state['user_input']['BP']
        cholesterol = st.session_state['user_input']['Cholesterol']
        na_to_k = st.session_state['user_input']['Na_to_K']

    predict_btn = st.button("🚀 Predict Drug", type="primary", use_container_width=True)

    if predict_btn:
        input_df = pd.DataFrame({
            'Age': [age],
            'Na_to_K': [na_to_k],
            'Sex_F': [1 if sex == "F" else 0],
            'Sex_M': [1 if sex == "M" else 0],
            'BP_HIGH': [1 if bp == "HIGH" else 0],
            'BP_LOW': [1 if bp == "LOW" else 0],
            'BP_NORMAL': [1 if bp == "NORMAL" else 0],
            'Cholesterol_HIGH': [1 if cholesterol == "HIGH" else 0],
            'Cholesterol_NORMAL': [1 if cholesterol == "NORMAL" else 0],
        })

        if apply_scaler and scaler:
            input_df[num_cols] = scaler.transform(input_df[num_cols])

        pred = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0]

        pred_label = mapp[pred]
        st.success(f"💊 **Predicted Drug:** {pred_label}")
        st.info(f"**Confidence:** {np.max(proba):.3f}")

        prob_df = pd.DataFrame({
            'Drug': [mapp[i] for i in range(1, 6)],
            'Probability': proba
        })
        fig = px.bar(prob_df, x='Drug', y='Probability', color='Drug',
                     title="Class Probabilities", text_auto='.3f')
        st.plotly_chart(fig, use_container_width=True)


main()