import streamlit as st
import codecs
import random 


def encode(inname):
    #st.write("works well")  # for test
    encode= codecs.encode(inname,"rot_13")
    return encode

def main():
    st.header("Hello, World! :sunglasses:")
    st.header("This was made to make you :red[Annoy]")
    st.header("Enjoy it! :smile:")
    st.header(":gray[If Its Possible] :smirk:")



def INTRODUCTION():
    st.title("Hi,:hand: welcome to introduction")
    st.header("How To Play:")
    st.subheader("Just Keep Play And Get Secret Code! ")
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
    
    inname=st.text_input("NAME:")
    #st.write(inname)
    if inname:
        #st.write(inname)
        encoded=encode(inname)
        if encoded!="hyunnn":
            st.write("Your Name Is",encoded,"Right? Hmm...")
        elif encoded=="hyunnn":
            st.write("Hello hyunnn! First Key Is 'K'")



def phone():
    st.title("Can I Get Your Phone Number? :iphone:") 

def birth():
    st.title("Let's Have a Party On Your Birthday! :partying_face:") 

if "age_ran" not in st.session_state:
    st.session_state.age_ran = random.randint(17, 60)

def age():
    st.title("How Old Are You? :smile:")
    st.write("let me guess...")
    st.write(st.session_state.age_ran, "?") 

    if st.button("NO"):
        st.session_state.age_ran = random.randint(17, 60)  # 새로운 랜덤 나이를 생성

    if st.button("YES"):
        if st.session_state.age_ran == 20:
            st.write("Oh Thanks for letting me know. The second key is 'I'")
        else:
            st.write("Hmm... Isn't that a lie?")
            
def VOLUME():
    st.title("Is This Enough For The Volume? :loud_sound:")

def SECRET():
    st.title("Secret? :lock:")
    key=st.text_input("Key:")
    if key=="KIVEIRU":
        st.write("Congratulation")
    else:
        st.write("That's not the Key")

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
#NAME: ROT13 ulhaaa