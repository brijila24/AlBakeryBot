import os
import sys
import importlib.util
import streamlit as st

st.write("Python version:", sys.version)
st.write("Current folder:", os.getcwd())
st.write("Files in current folder:", os.listdir("."))
st.write("requirements.txt exists:", os.path.isfile("requirements.txt"))
st.write("google-genai installed:", importlib.util.find_spec("google.genai") is not None)