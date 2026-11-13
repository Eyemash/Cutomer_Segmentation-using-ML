import streamlit as st
import pandas as pd
import numpy as np
import joblib 

kmeans =joblib.load("kmeans_model.pkl") # Load the pre-trained KMeans model
scaler = joblib.load("scaler.pkl") # Load the pre-trained scaler

st.title("Customer Segmentation App")
st.write("Enter customer details to predict the segment")

age = st.number_input("Age", min_value=18, max_value=100 ,value=35)
income = st.number_input("Income", min_value=0, max_value=2000000, value=50000)
total_spending = st.number_input("Total Spending(sum of purchases)", min_value=0, max_value=5000, value = 1000)
num_web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=100, value = 10)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=100, value = 10)
num_web_visits = st.number_input("Number of Web Visits", min_value=0, max_value=50, value = 3)
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value = 30)


imput_data = pd.DataFrame({
    "Age" :[age],
    "Income" :[income],
    "total_spending":[total_spending],
    "numwebpurchases":[num_web_purchases],
    "numstorepurchases":[num_store_purchases],
    "numwebvisitsMonth":[num_web_visits],
    "recency":[recency]
    })

input_scaled = scaler.transform(imput_data) # Scale the input data

if st.button("Predict Segment"):

    cluster = kmeans.predict(input_scaled) # Predict the segment

    st.success(f"predicted segment: Cluster {cluster}")


    