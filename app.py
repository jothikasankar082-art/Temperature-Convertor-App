import streamlit as st

st.title("🌡️ Temperature Converter")

# Input temperature
temp = st.number_input("Enter temperature:")

# Choose conversion type
choice = st.radio("Convert from:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Button to convert
if st.button("Convert"):
    if choice == "Celsius to Fahrenheit":
        result = (temp * 9/5) + 32
        st.success(f"{temp}°C = {result:.2f}°F")
    else:
        result = (temp - 32) * 5/9
        st.success(f"{temp}°F = {result:.2f}°C")
