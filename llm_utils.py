
import sys
import importlib.metadata

print("Python:", sys.executable)

try:
    print("Installed SDK version:",
          importlib.metadata.version("google-genai"))
except Exception as e:
    print("SDK installation problem:", repr(e))

try:
    from google import genai
    print("IMPORT SUCCESS")
except Exception as e:
    print("IMPORT FAILED:", repr(e))
    raise
