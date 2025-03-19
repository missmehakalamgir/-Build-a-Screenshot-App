import streamlit as st
from streamlit_drawable_canvas import st_canvas
import mss
import numpy as np
from PIL import Image

# Title of the app
st.title("Customizable Screenshot Tool")

st.write("Draw a rectangle on the canvas to select the area for the screenshot.")

# Canvas settings for drawing
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",  
    stroke_width=3,
    stroke_color="red",
    background_color="white",
    height=400,
    width=600,
    drawing_mode="rect",
    key="canvas",
)

# Button to capture screenshot
if st.button("Take Screenshot"):
    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if len(objects) > 0:
            rect = objects[0]
            left = int(rect["left"])
            top = int(rect["top"])
            width = int(rect["width"])
            height = int(rect["height"])

            # Capture the screen using mss
            with mss.mss() as sct:
                screenshot = sct.grab(sct.monitors[1])  # Capture the first screen
                img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

                # Crop the screenshot based on user selection
                cropped_screenshot = img.crop((left, top, left + width, top + height))

                # Save and display
                cropped_screenshot.save("cropped_screenshot.png")
                st.success("Cropped screenshot saved as cropped_screenshot.png")
                st.image(cropped_screenshot, caption="Cropped Screenshot", use_column_width=True)
        else:
            st.warning("Please draw a rectangle on the canvas before taking a screenshot.")
    else:
        st.warning("Canvas is empty. Please draw a rectangle.")
