import streamlit as st

st.title("BMI Calculator")
st.write("This app calculates your Body Mass Index (BMI) based on your weight and height.")

#Get user input for weight and height
weight = st.number_input("Enter your weight in kilograms:", min_value=1.0, step=0.1)
height = st.number_input("Enter your height in meters:", min_value=0.1, step=0.01)  


#Button to calculate BMI
if st.button("Calculate BMI"):
    if height <= 0:
        st.error("Height must be greater than zero.")
    else:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        st.write(f"You are classified as: {category}")
        
        
# Add more information about BMI
email = st.text_input("Enter your email to receive more information about BMI and health tips:", "")
if email:
    st.success("Thank you! You will receive more information about BMI and health tips at your email address.")