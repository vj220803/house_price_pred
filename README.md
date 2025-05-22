# **House Price Prediction (sqaure feet)**
Creating a simple House Price Prediction Streamlit App

A simple yet effective **Machine Learning app** built using **Streamlit** that predicts house prices based on size (in square feet). This project demonstrates the use of **Linear Regression** for a regression task, making it ideal for beginners in Data Science and ML.

## Overview
This app uses a small sample dataset to train a Linear Regression model, which predicts the price of a house given its size. The app is deployed using **Streamlit Cloud**, and allows users to input square footage to get real-time predictions.

## Flow of App Deployement
![flow](https://github.com/vj220803/house_price_pred-single_feature-/blob/main/Building_app.png)

## Features
- Simple and clean Streamlit web interface
- Uses scikit-learn’s `LinearRegression` for model training
- Real-time user input for predictions
- Model accuracy displayed using **Mean Absolute Error (MAE)**

## Tech Stack
| Technology     | Description                    |
|----------------|--------------------------------|
| Python         | Core programming language      |
| Streamlit      | Web framework for ML apps      |
| scikit-learn   | Model building & evaluation    |
| pandas         | Data handling                  |
| Git & GitHub   | Version control & deployment   |

## Project Structure

![project_strucutre]()

```
house_price_app/
│
├── house_price.py # Main Streamlit app
├── requirements.txt # Required Python libraries
├── README.md # Project documentation (current file)

``` 
---------

## Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/vj220803/house_price_pred.git
   cd house_price_pred

#### Creating a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### **Run Locally**
streamlit run house_price.py

### **Deployment on Streamlit Cloud**
-Push your code to GitHub.
-Go to https://streamlit.io/cloud
-Click on "Deploy an App".
-Select your GitHub repo and branch (main or master).
-Set the main file path to: house_price.py
-Set the requirements file path to: requirements.txt
-Click "Deploy".

## **Sample Dataset**
| Size (sq ft) | Price (in lakhs) |
| ------------ | ---------------- |
| 750          | 35               |
| 800          | 38               |
| ...          | ...              |
| 1400         | 85               |

## **Author**
Vijayan Naidu 
Student at @ Fergusson College, Pune

## **Screenshot**
![house_price_ss](https://github.com/vj220803/house_price_pred-single_feature-/blob/main/house_price(single_feature)_UI.PNG)
https://1drv.ms/i/c/0dc8d4ddd66f20c7/ESIWqpYy0L9HkT7L-TjAa9YBVq-A_BUqC5Ez7_OoqSbBrA?e=sWXVi0







