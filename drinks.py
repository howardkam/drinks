import streamlit as st
import subprocess

st.title("Streamlit App to Run Another Python Script")

# Define a button to run another script
if st.button("Run Another Script"):
    result = subprocess.run(["python", "drinks-master.py"], capture_output=True, text=True)
    
    st.subheader("Output:")
    st.code(result.stdout)