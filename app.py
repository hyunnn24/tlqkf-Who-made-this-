import streamlit as st

def main():
    st.title("Hello, World")
    st.write("This page was made to make you angry. Please enjoy it!")

def phone():
    st.write("Phone Number Page")  # Placeholder content

def birth():
    st.write("Birth Day Page")  # Placeholder content

def age():
    st.write("Age Page")  # Placeholder content

page = st.sidebar.selectbox("LET'S GET THE KING :)", ["MAIN","PHONE NUMBER", "BIRTH DAY", "AGE"])

if page == "PHONE NUMBER":
    phone()
elif page == "BIRTH DAY":
    birth()
elif page == "AGE":
    age()
elif page == "MAIN":
    main()
