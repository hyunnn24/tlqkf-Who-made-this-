import streamlit as st

def main():
    st.header("Hello, World! :sunglasses:")
    st.header("This was made to make you :red[Annoy]")
    st.header("Enjoy it! :smile:")
    st.header(":gray[If Its Possible] :smirk:")

def INTRODUCTION():
    st.title("Hi,:hand: welcome to introduction")
    st.header("How To Play:")
    st.subheader("Just Keep Play And Get Secret Code! ")
    st.subheader("In order to continue")
    st.subheader("You have to memorize this")
def phone():
    st.title("Can I Get Your Phone Number? :iphone:") 

def birth():
    st.title("Let's Have a Party On Your Birthday! :partying_face:") 

def age():
    st.title("How Old Are You? :smile:")  

def VOLUME():
    st.title("Is This Enough For The Volume? :loud_sound:")

def SECRET():
    st.title("Do You Want To Know The Secret? :lock:")

page = st.sidebar.selectbox("LET'S GET THE KING :)", ["MAIN","INTRODUCTION","PHONE NUMBER", "BIRTH DAY", "AGE","VOLUME","SECRET"])
st.sidebar.text("  made by hyunnn :kr: \n  CERT-IS PKNU \n  2024.08.13")

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
elif page == "SECRET":
    SECRET()
elif page == "INTRODUCTION":
    #SECRET CODE: KIVEIRU 