import streamlit as st
import time as t

#title
st.title("Welcome to my TEST PAGE")

#image
st.image("Johnson.jpeg")

#Header
st.header("Machine Learning")

st.subheader("Linear Regression")

st.info("Information details of user")

st.warning("Come early or else you would be marked absent")

st.error("Wrong Password")

st.success("Congratulations! You Passed")

st.write("Employee Name:")
st.write(range(100))

st.markdown("Johnson Amodu")
st.markdown("# Johnson Amodu")
st.markdown("## Johnson Amodu")
st.markdown("#### Johnson Amodu")

#Emoji
st.markdown(":moon:")

st.text("Welcome to my Data Science Page")

#To write caption
st.caption("Caption is here")

#To display Mathematical expression
st.latex(r''' a + bx^2 + c''')

#Widget
st.checkbox('Login')
st.button("Click")
st.radio("Pick your gender", ['Male',"Female",'Other'])
st.selectbox("Pick your course",['Data Engrg',"Data Analytics",'Data Science'])
st.multiselect("Choose your dept",['Operations','Finance','HR','QA'])
st.select_slider("Rating",['Poor','Bad','Average','Good','Excellent'])
st.slider("Enter your Score",0,10)
st.number_input("Pick a number",0,100)
st.text_input("Enter your emaill address:")
st.date_input("Opening Ceremony")
st.time_input("Select your time")
st.text_area("Please enter your comment here:")
st.file_uploader("Upload your file here:")
st.color_picker("Select any colour")
st.progress(80)

#Spinner
with st.spinner("Loading...Please wait"):
    t.sleep(3)

#ballons
st.balloons()

#sidebar
st.sidebar.title("Tehillah")
st.sidebar.text_input("Email Address:")
st.sidebar.text_input("Password:")
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert",['Entry Level','Associate','Lead','Manager','Senior Manager','Expert','Consultant'])

#Data Visualization
import pandas as pd
import numpy as np

st.title("Bar Chart")
data = pd.DataFrame(np.random.randn(50,2), columns=['x','y'])
st.bar_chart(data)

st.title("Linechart")
st.line_chart(data)

st.title("Areachart")
st.area_chart(data)

