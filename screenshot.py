import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

# Title of the app
st.title("Upload & Crop Screenshot Tool")

st.write("Upload an image and draw a rectangle to crop the selected area.")

# File uploader for the user to upload an image
uploaded_file = st.file_uploader("Upload a Screenshot", type=["png", "jpg", "jpeg"])

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

# Button to crop the uploaded image
if st.button("Crop Screenshot"):
    if uploaded_file is not None:
        if canvas_result.json_data is not None:
            objects = canvas_result.json_data["objects"]
            if len(objects) > 0:
                rect = objects[0]
                left = int(rect["left"])
                top = int(rect["top"])
                width = int(rect["width"])
                height = int(rect["height"])

                # Open uploaded image
                image = Image.open(uploaded_file)

                # Crop the image based on user selection
                cropped_image = image.crop((left, top, left + width, top + height))

                # Save and display the cropped image
                cropped_image.save("cropped_screenshot.png")
                st.success("Cropped screenshot saved as cropped_screenshot.png")
                st.image(cropped_image, caption="Cropped Screenshot", use_column_width=True)
            else:
                st.warning("Please draw a rectangle on the canvas before cropping the image.")
        else:
            st.warning("Canvas is empty. Please draw a rectangle.")
    else:
        st.warning("Please upload a screenshot first.")
