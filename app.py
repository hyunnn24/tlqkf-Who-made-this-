import streamlit as st
import base64

def encode(inname):
    # Encode input name to Base64
    inname_bytes = inname.encode('utf-8')  # Convert to bytes
    encoded_bytes = base64.b64encode(inname_bytes)  # Base64 encode
    encoded_str = encoded_bytes.decode('utf-8')  # Convert bytes back to string
    return encoded_str

def decode(encoded_name):
    # Decode Base64 to original name
    encoded_bytes = encoded_name.encode('utf-8')  # Convert to bytes
    decoded_bytes = base64.b64decode(encoded_bytes)  # Base64 decode
    decoded_str = decoded_bytes.decode('utf-8')  # Convert bytes back to string
    return decoded_str

def main():
    st.header("Hello, World! :sunglasses:")
    st.header("This was made to make you :red[Annoy]")
    st.header("Enjoy it! :smile:")
    st.header(":gray[If Its Possible] :smirk:")

def INTRODUCTION():
    st.title("Hi,:hand: welcome to introduction")
    st.header("How To Play:")
    st.subheader("Just Keep Play And Get Secret Code!")
    st.write()
    st.header("In order to continue:")
    st.subheader("You have to memorize this")
    st.subheader("Hi, my name is hyunnn and I am 20 years old!")
    st.subheader("My birthday is May 2nd, 2005(fake)")
    st.subheader("The phone number is 010 2535 4362(fake)")
    st.subheader("I like to listen to music at exactly 50% volume")
    st.subheader("And My birthday is May 2nd, 2005!")

def name():
    st.title("Hi :raised_hands: Nice To Meet You Whats Your Name?")
    
    inname = st.text_input("NAME:")
    if inname:
        encoded = encode(inname)
        decoded_name = decode(encoded)
        if encoded != "hyunnn":
            st.write("Your Name Is", encoded, "Right? Hmm...")
        elif encoded == "hyunnn":
            st.write("Hello hyunnn! First Key Is 'K'")
#Base64 encoded string for 'hyunnn': aHl1bm5u
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

page = st.sidebar.selectbox("LET'S GET THE KING :)", ["MAIN","INTRODUCTION","NAME","PHONE NUMBER", "BIRTH DAY", "AGE","VOLUME","SECRET"])
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
    INTRODUCTION()
elif page == "NAME":
    name()
#SECRET CODE: KIVEIRU