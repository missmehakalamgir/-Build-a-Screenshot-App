import streamlit as st
import pyautogui
import time
from PIL import Image

st.title("🖼️ Screenshot App with Mouse Selection")

st.write("Click the button below to take a screenshot by selecting an area with your mouse.")

if st.button("Take Screenshot"):
    st.write("Select the area to capture...")
    time.sleep(2)  # Delay to allow selection
    
    # Capture selected region using mouse
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    
    st.image("screenshot.png", caption="Captured Screenshot", use_column_width=True)
    
    with open("screenshot.png", "rb") as file:
        btn = st.download_button(
            label="Download Screenshot",
            data=file,
            file_name="screenshot.png",
            mime="image/png"
        )
