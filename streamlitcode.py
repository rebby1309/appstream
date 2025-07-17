import streamlit as st

# Title of the app
st.title("My First Streamlit App 🎉")

# Header
st.header("Welcome to Streamlit!")

# Text
st.write("This is a basic Streamlit app to get you started.")

# Input
name = st.text_input("What's your name?")

# Button
if st.button("Say Hello"):
    st.success(f"Hello, {name} 👋")

# Slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You're {age} years old.")

# Checkbox
if st.checkbox("Show secret message"):
    st.info("🕵️ The cake is a lie.")

# Select box
color = st.selectbox("Pick a color", ["Red", "Green", "Blue"])
st.write(f"You chose: {color}")
