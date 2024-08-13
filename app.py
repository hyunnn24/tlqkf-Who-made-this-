import streamlit as st

def main():
    st.header("Hello, World! :sunglasses:")
    st.header("This was made to make you :red[Annoy]")
    st.header("Enjoy it! :smile:")
    
def phone():
    st.title("Can I Get Your Phone Number? :smile:") 

def birth():
    st.title("Let's Have a Party On Your Birthday! :smile:") 

def age():
    st.title("How Old Are You? :smile:")  

def VOLUME():
    st.title("Is This Enough For The Volume? :smile:")


page = st.sidebar.selectbox("LET'S GET THE KING :)", ["MAIN","PHONE NUMBER", "BIRTH DAY", "AGE","VOLUME"])
st.sidebar.text("  made by hyunnn \n  CERT-IS PKNU \n  2024.08.13")

if page == "PHONE NUMBER":
    phone()
elif page == "BIRTH DAY":
    birth()
elif page == "AGE":
    age()
elif page == "MAIN":
    main()
elif page == "VOLUME":
    VOLUME()