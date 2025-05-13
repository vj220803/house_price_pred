import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Title
st.title("House Price Prediction App")

# Sample Dataset
data = {
    "Size (sq ft)": [750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400],
    "Price (in lakhs)": [35, 38, 40, 45, 50, 55, 60, 68, 75, 85]
}
df = pd.DataFrame(data)

# Display the dataset
st.write("### Sample House Prices Dataset")
st.write(df)

# Split the data
X = df[["Size (sq ft)"]]
y = df["Price (in lakhs)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
error = mean_absolute_error(y_test, y_pred)

st.write(f"### Model Accuracy: MAE = {error:.2f} lakhs")

# User input
st.sidebar.header("Enter House Details")
sq_ft = st.sidebar.number_input("Size (sq ft)", min_value=500, max_value=2000, value=1000, step=50)

# Predict
if st.sidebar.button("Predict Price"):
    prediction = model.predict([[sq_ft]])[0]
    st.sidebar.write(f"### Predicted Price: {prediction:.2f} lakhs")

# Instructions to Deploy
st.write("### Deployment Instructions")
st.write("1. Install dependencies using `pip install streamlit pandas scikit-learn`")
st.write("2. Run the app locally using `streamlit run app.py`")
st.write("3. Deploy to [Streamlit Community Cloud](https://streamlit.io/cloud)")
