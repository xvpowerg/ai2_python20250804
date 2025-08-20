import streamlit as st
st.title("Number Input")
n1 = st.number_input("Enter First Number:",value=0)
n2 = st.number_input("Enter Second Number:",value=0)
sum_result = n1 + n2
st.write(f"The sum is:{sum_result}")