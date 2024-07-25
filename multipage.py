import streamlit as st

def home():
    st.title("Home")
    st.write("welcome")
def about_me():
    st.title("ABOUT ME")
    st.write("Hey i am dasha and i love to eat")

def contact_me():
    st.title("Contact")
    st.write("why do u want to contact me?? ")

#navigation begins
st.sidebar.title("Navigation")
page=st.sidebar.radio("go to ",["Home","ABOUT ME","CONTACT"])

if page=="Home":
    home()
elif page=="ABOUT ME":
    about_me()
else:
    contact_me()        