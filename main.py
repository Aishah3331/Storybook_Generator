import streamlit as st

st.title("This is a title")
st.write("This is a **text** :books:")

st.button('Reset', type="primary")
if st.button('say hello!'):
  st.write("why hello there")
else:
  st.write("goodbye")
