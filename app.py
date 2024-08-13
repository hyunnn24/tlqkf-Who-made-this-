import streamlit as st


def main():
    st.title("Hello, World")
def phone():

def birth():

def age():

page = st.sidebar.selectbox("LET'S GET THE KING :)", ["MAIN","PHONE NUMBER", "BIRTH DAY", "AGE"])

if page == "PHONE NUMBER":
    phone()
elif page == "BIRTH DAY":
    birth()
elif page == "AGE":
    age()
elif page == "MAIN":
    main()