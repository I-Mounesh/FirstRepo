import streamlit as st
import pandas as pd
import pickle
# Load the pickled model
model = pickle.load(open("model.pkl", "rb"))
# Read the cleaned data
df = pd.read_csv("../data/Bengaluru_House_Data_Cleaned.csv")

st.title("Bengaluru House Price Prediction")


# Select location from the available options in the dataset
location = st.selectbox("Location", df["location"].unique())

# Input fields for the other features
total_sqft = st.number_input("Total Square Feet", min_value=0.0, value=1000.0)
bath = st.number_input("Number of Bathrooms", min_value=1, value=2)
bhk = st.number_input("Number of Bedrooms", min_value=1, value=2)

# Predict the price
if st.button("Predict"):
    # Create a DataFrame from the input features
    input_data = pd.DataFrame(
        [[location, total_sqft, bath, bhk]],
        columns=["location", "total_sqft", "bath", "bhk"],
    )

    # Make the prediction
    prediction = model.predict(input_data)

    # Convert price from millions to lakhs and round to the nearest lakh
    rounded_prediction_lakhs = round(prediction[0] * 100000)

    # Format the prediction for display
    formatted_prediction = (
        f"₹{rounded_prediction_lakhs:,.0f} "  # Format in Lakhs with commas
    )

    # Display the formatted price
    st.write(f"The predicted price is: {formatted_prediction}")

# Display additional information
st.subheader("Additional Information")
st.write("This app predicts the price of a real estate property based on its features.")
st.write("The model was trained on the Bengaluru House Price dataset.")

