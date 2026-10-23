
import sys
import importlib.metadata
import streamlit as st

st.title("Google GenAI Diagnostic")

st.write("Python:", sys.executable)

try:
    version = importlib.metadata.version("google-genai")
    st.write("Google GenAI version:", version)
except Exception as e:
    st.error(f"Package not installed: {e}")

try:
    from google import genai
    st.success("Google GenAI import successful!")
except Exception as e:
    st.error(f"Google GenAI import failed: {e}")
    try:
        import google
        st.write("Google module file:", getattr(google, "__file__", None))
        st.write("Google paths:", list(getattr(google, "__path__", [])))
    except Exception as inner_e:
        st.write("Google module error:", repr(inner_e))
