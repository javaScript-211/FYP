from streamlit.testing.v1 import AppTest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(multiEmoteFt.py)))  # Add current directory to path


def test_app():
    at = AppTest.from_file("Home.py").run()    
   