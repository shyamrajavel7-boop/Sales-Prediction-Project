import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load and train model
@st.cache_data
def load_and_train():
    df = pd.read_csv("Advertising.csv")
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    
    X = df[["TV", "Radio", "Newspaper"]]
    y = df["Sales"]
    
    model = LinearRegression()
    model.fit(X, y)
    return model, df

model, df = load_and_train()

# Title
st.title("📊 Sales Prediction System")

# Explanation
st.write("""
Based on the entered advertising budgets, the machine learning
model estimates the expected sales.
""")

# Input fields
st.sidebar.header("Input Advertising Budgets")
tv_budget = st.sidebar.number_input("TV Advertising Budget", min_value=0.0, value=100.0)
radio_budget = st.sidebar.number_input("Radio Advertising Budget", min_value=0.0, value=50.0)
newspaper_budget = st.sidebar.number_input("Newspaper Advertising Budget", min_value=0.0, value=25.0)

# Prediction button
if st.sidebar.button("Predict Sales"):
    new_data = pd.DataFrame({
        "TV": [tv_budget],
        "Radio": [radio_budget],
        "Newspaper": [newspaper_budget]
    })
    
    prediction = model.predict(new_data)[0]
    
    st.subheader("Prediction Result")
    st.success(f"Predicted Sales: {prediction:.2f}")

    # Visualization of Impact
    st.subheader("Advertising Impact Breakdown")
    coefficients = model.coef_
    
    # Calculate contribution for the given input
    contributions = [tv_budget * coefficients[0], radio_budget * coefficients[1], newspaper_budget * coefficients[2]]
    labels = ["TV Impact", "Radio Impact", "Newspaper Impact"]
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=labels, y=contributions, palette="magma", ax=ax)
    ax.set_ylabel("Impact on Sales")
    st.pyplot(fig)
