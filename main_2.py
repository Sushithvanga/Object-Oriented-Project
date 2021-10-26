import streamlit as st

st.title("This is the experimental GUI for understanding")
st.markdown("This GUI consists of all the feature experimentation of streamlit APIs")

st.radio("Select the option",[1,2,3])
st.text_input("Enter some value")
st.button("Apply the following settings")

st.checkbox("Check this out")

st.sidebar.slider("Select the number",min_value=0,max_value=10)

st.selectbox("Select the option wanted",("Cat","Dog"))

st.button("Check-in","Checkout")

