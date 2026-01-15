import streamlit as st

# streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power")

n = st.number_input("Enter an integer", value=1, step=1)

# calculate = n**2 
Square = n**2
cube = n ** 3
fifth_power = n**5

# display result
st.write(f"The square of {n} is: {Square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is :{fifth_power}")