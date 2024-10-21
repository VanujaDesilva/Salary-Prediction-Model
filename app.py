import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction App")

st.divider()

st.write("With this app, you can get estimated salaries of the company employees ")

years = st.number_input("Enter the No of years at company",value= 1, step=1,min_value=0)
jobrate = st.number_input("Enter the job rate",value= 3.5, step=0.5,min_value=0.0)

model = joblib.load("linearmodel.pkl")
X = [years, jobrate]

predict = st.button("Press the button for salart prediction")

st.divider()
if predict:

    st.balloons()

    X1 = np.array([X])

    prediction = model.predict(X1)[0]

    st.write(f"Salary prediction is{prediction:,.2f}")

    st.divider()

