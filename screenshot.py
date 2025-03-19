import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pyautogui
from PIL import Image

# Title of the app
st.title("Customizable Screenshot Tool")

# Instructions for the user
st.write("Draw a rectangle on the canvas to select the area for the screenshot.")

# Canvas settings for drawing
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",  # Transparent background
    stroke_width=3,
    stroke_color="red",
    background_color="white",
    height=400,
    width=600,
    drawing_mode="rect",  # Allow user to draw rectangles
    key="canvas",
)

# Button to capture screenshot
if st.button("Take Screenshot"):
    if canvas_result.json_data is not None:
        # Get rectangle coordinates from canvas
        objects = canvas_result.json_data["objects"]
        if len(objects) > 0:
            rect = objects[0]  # Taking the first rectangle drawn
            left = int(rect["left"])
            top = int(rect["top"])
            width = int(rect["width"])
            height = int(rect["height"])

            # Capture the full screen screenshot
            screenshot = pyautogui.screenshot()

            # Crop the screenshot based on user selection
            cropped_screenshot = screenshot.crop((left, top, left + width, top + height))

            # Save the cropped screenshot
            cropped_screenshot.save("cropped_screenshot.png")

            # Show success message
            st.success("Cropped screenshot saved as cropped_screenshot.png")

            # Display the cropped screenshot
            img = Image.open("cropped_screenshot.png")
            st.image(img, caption="Cropped Screenshot", use_column_width=True)
        else:
            st.warning("Please draw a rectangle on the canvas before taking a screenshot.")
    else:
        st.warning("Canvas is empty. Please draw a rectangle.")

