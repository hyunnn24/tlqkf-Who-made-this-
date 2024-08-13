import streamlit as st

page = st.sidebar.selectbox("GET THE KING", ["MAIN","PHONE NUMBER", "BIRTH DAY", "AGE"])

if page == "PHONE NUMBER":
    phone()
elif page == "BIRTH DAY":
    birth()
elif page == "AGE":
    age()
elif page == "MAIN":
    main()

def main():
    st.write("Hello, World")
def phone():

def birth():

def age():