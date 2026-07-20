import math
import streamlit as st

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Advanced Calculator")

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

operation = st.selectbox(
    "Select Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Modulus",
        "Power",
        "Square Root",
        "Log10",
        "Natural Log",
        "Sin",
        "Cos",
        "Tan",
        "Factorial",
        "Absolute Value",
    ],
)

# Two-number operations
if operation in [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Modulus",
    "Power",
]:
    num1 = st.number_input("First Number", value=0.0)
    num2 = st.number_input("Second Number", value=0.0)

# Single-number operations
else:
    num1 = st.number_input("Enter Number", value=0.0)

if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
            expression = f"{num1} + {num2}"

        elif operation == "Subtraction":
            result = num1 - num2
            expression = f"{num1} - {num2}"

        elif operation == "Multiplication":
            result = num1 * num2
            expression = f"{num1} × {num2}"

        elif operation == "Division":
            if num2 == 0:
                st.error("Division by zero is not allowed.")
                st.stop()
            result = num1 / num2
            expression = f"{num1} ÷ {num2}"

        elif operation == "Modulus":
            result = num1 % num2
            expression = f"{num1} % {num2}"

        elif operation == "Power":
            result = num1 ** num2
            expression = f"{num1}^{num2}"

        elif operation == "Square Root":
            if num1 < 0:
                st.error("Cannot calculate square root of a negative number.")
                st.stop()
            result = math.sqrt(num1)
            expression = f"√({num1})"

        elif operation == "Log10":
            if num1 <= 0:
                st.error("Log10 is only defined for positive numbers.")
                st.stop()
            result = math.log10(num1)
            expression = f"log10({num1})"

        elif operation == "Natural Log":
            if num1 <= 0:
                st.error("Natural log is only defined for positive numbers.")
                st.stop()
            result = math.log(num1)
            expression = f"ln({num1})"

        elif operation == "Sin":
            result = math.sin(math.radians(num1))
            expression = f"sin({num1}°)"

        elif operation == "Cos":
            result = math.cos(math.radians(num1))
            expression = f"cos({num1}°)"

        elif operation == "Tan":
            result = math.tan(math.radians(num1))
            expression = f"tan({num1}°)"

        elif operation == "Factorial":
            if num1 < 0 or not float(num1).is_integer():
                st.error("Factorial requires a non-negative integer.")
                st.stop()
            result = math.factorial(int(num1))
            expression = f"{int(num1)}!"

        elif operation == "Absolute Value":
            result = abs(num1)
            expression = f"|{num1}|"

        st.success(f"Result: {result}")

        st.session_state.history.append(f"{expression} = {result}")

    except Exception as e:
        st.error(f"Error: {e}")

st.divider()

st.subheader("📜 Calculation History")

if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.write(item)
else:
    st.info("No calculations yet.")

col1, col2 = st.columns(2)

with col1:
    if st.button("🗑 Clear History"):
        st.session_state.history = []
        st.rerun()

with col2:
    if st.button("📋 Show Total Calculations"):
        st.info(f"Total calculations: {len(st.session_state.history)}")