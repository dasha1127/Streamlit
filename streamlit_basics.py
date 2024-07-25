import streamlit as st
#title
st.title("Hello dasha")

#header and subheader
st.header("How r u")
st.subheader("I am goooddd")

#text
st.text("I am useless")

#markdown means adjusts the sixe the texts
st.markdown("# This is dasha")
st.markdown("## This is dasha1")
st.markdown("### This is dasha2")
st.markdown("#### This is dasha3")

#success,info,warning,error,exception
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

#write
st.write("blah blah blah")

from PIL import Image
#not sure about the file type like jpg and jpeg but worked on only png
img=Image.open("pic1.png")
st.image(img,width=300)

#checkbox returns a boolean value, when the box is checked 
if st.checkbox("show/hide"):

    st.text("showing the widget")

#radio button has 2 argumnets
#1) title of the radio button
#2) options for the radio button
status=st.radio("select gender:",('male','female'))
if (status == 'male'):
    st.success("male")
else:
    st.success("female")

#selection box
colors=st.selectbox("COLORS:",['PURPLE','ORANGE','red','white'])
st.write("MY fav colors id:",colors)    

#multi-selectbox:
colors=st.multiselect("COLORS:",['PURPLE','ORANGE','red','white'])
st.write("i have",len(colors),'colors bottles')

#button
if(st.button("Click me")):
    st.text("yoo you are cute")

#text input
name = st.text_input("Enter Your name", "Type Here ...")
if(st.button('Submit')):
    result = name.title()
    st.success(result)

#slider
#1) title of the slider
#2)strting of the slider
#3) ending of the slider
level = st.slider("Select the level", 1, 10)
st.text('Selected: {}'.format(level))


          
