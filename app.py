import streamlit as st

def main():
    st.header("Hello, World! :sunglasses:")
    st.header("This was made to make you :red[Annoy]")
    st.header("Enjoy it! :smile:")
    
def phone():
    st.write("Phone Number Page")  # Placeholder content

def birth():
    st.write("Birth Day Page")  # Placeholder content

def age():
    st.write("Age Page")  # Placeholder content

page = st.sidebar.selectbox("LET'S GET THE KING :) \n made by hyunnn CERT-IS PKNU 2024.08.13", ["MAIN","PHONE NUMBER", "BIRTH DAY", "AGE"])

if page == "PHONE NUMBER":
    phone()
elif page == "BIRTH DAY":
    birth()
elif page == "AGE":
    age()
elif page == "MAIN":
    main()
