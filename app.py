import streamlit as st
import numpy as np
from joblib import load

# Example of applying a custom theme
st.set_page_config(
    page_title="Employee Performance Rate",
    page_icon=":chart_with_upwards_trend:",
    layout="centered",  # Set the layout to wide for a more spacious design
)

# Example of using custom CSS for styling
st.markdown(
    """
    <style>
    /* Define custom CSS styles */
    body {
        background-image: url('https://storage.googleapis.com/profit-prod/wp-content/uploads/2021/03/68e656fb-5ways-effective-performance-appraisal-system.jpg'); /* Set the background image */
        background-size: cover;
        font-family: Times New Roman;  /* Change the font family */
        opacity: 0.8;
    }
    .stApp {
        max-width: 5000px;  /* Set maximum width */
    }
    .stSlider > div > div > div > div {
        background-color: #008CBA; /* Set slider track color */
        border-radius: 10px;
    }
    .stButton > button {
        color: white; /* Set button text color */
        background-color: #008CBA;  /* Set button background color */
        border-radius: 10px;  /* Add border radius to buttons */
        padding: 8px 16px; /* Add padding to button */
        font-size: 16px; /* Increase font size of button */
    }
    .col2_container {
        padding-left: 20px;  /* Add space between col1 and col2 */
    }

    </style>
    """,
    unsafe_allow_html=True
)

loaded_model = load("unnati_model.sav")

def predict(data):
    return loaded_model.predict(data)

def performance_category(prediction):
    if prediction < 0.3:
        return "Poor Performance - Improvement Needed"
    elif prediction >= 0.3 and prediction < 0.5:
        return "Average Performance"
    else:
        return "Good Performance"

st.title("Employee Attrition Rate")

col1, col2 = st.columns(2)
with col1:
    el = st.slider("Education Level", 1, 5, 3)
    tos = st.slider("Time of Service", 1, 100, 2)
    top = st.slider("Time of Promotion", 0, 50, 5)
    gr = st.slider("Growth Rate", 0, 74, 37)

with col2:
    tr = st.selectbox("Travel Rate", [0, 1, 2])
    pl = st.selectbox("Post Level", [1, 2, 3, 4, 5])

if st.button("Predict Performance Rate"):
    st.write("Employee Performance Rate is : ")
    result = predict(np.array([[el, tos, top, gr, tr, pl, 1, 1, 1, 1, 1]]))[0]
    category = performance_category(result)
    st.markdown(f"**Performance Rate:** {result}")
    st.markdown(f"**Performance Category:** {category}")
