import streamlit as st

# Title
st.title("My First Streamlit App")

# Text
st.write("Welcome to Streamlit!")

# User Input
name = st.text_input("Enter your name:")

# Button
if st.button("Submit"):
    st.success(f"Hello, {name}!")

# Slider
age = st.slider("Select your age:", 1, 100, 25)

st.write("Your age is:", age)
