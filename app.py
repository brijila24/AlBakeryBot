
import os
import sys
import importlib.metadata as metadata
import streamlit as st

st.title("Bakery Bot - Deployment Diagnostic")

st.write("Python version:", sys.version)
st.write("App folder:", os.getcwd())

req_path = os.path.join(os.getcwd(), "requirements.txt")

st.write("requirements.txt exists:", os.path.exists(req_path))

if os.path.exists(req_path):
    with open(req_path, "r", encoding="utf-8") as f:
        st.code(f.read())

try:
    version = metadata.version("google-genai")
    st.success(f"google-genai installed: {version}")
except metadata.PackageNotFoundError:
    st.error("google-genai is NOT installed")

try:
    from google import genai
    st.success("Google GenAI import successful")
except Exception as e:
    st.error(f"Google GenAI import failed: {e}")
