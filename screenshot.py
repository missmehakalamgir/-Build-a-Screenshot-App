import streamlit as st
import mss
import time
from PIL import Image

st.title("🖼️ Screenshot App with Mouse Selection")

st.write("Click the button below to take a screenshot of your screen.")

if st.button("Take Screenshot"):
    st.write("Capturing screenshot...")
    time.sleep(2)  # Delay to allow selection
    
    with mss.mss() as sct:
        screenshot_filename = sct.shot(output="screenshot.png")
    
    st.image("screenshot.png", caption="Captured Screenshot", use_column_width=True)
    
    with open("screenshot.png", "rb") as file:
        st.download_button(
            label="Download Screenshot",
            data=file,
            file_name="screenshot.png",
            mime="image/png"
        )
