import streamlit as st

def main():
    st.header("Hello, World! :sunglasses:")
    st.header("This was made to make you :red[Annoy]")
    st.header("Enjoy it! :smile:")
    
def phone():
    st.title("Can I Get Your Phone Number? :laugh:") 

def birth():
    st.write("Birth Day Page") 

def age():
    st.write("Age Page")  

def VOLUME():
    st.write(" volume page")


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