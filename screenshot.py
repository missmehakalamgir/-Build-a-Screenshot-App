import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

st.title("📸 Screenshot Cropper")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Open image
    img = Image.open(uploaded_file)
    img = img.convert("RGB")  # Convert to RGB (fix some issues with transparency)
    img_array = np.array(img)

    st.image(img, caption="Original Image", use_column_width=True)

    # Canvas settings
    st.write("🎨 Draw a selection to crop:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Transparent orange
        stroke_width=2,
        stroke_color="red",
        background_image=img,  # Pass the PIL image
        update_streamlit=True,
        height=img.height // 2,  # Adjust to show part of the image
        width=img.width // 2,
        drawing_mode="rect",  # Rectangular selection
        key="canvas",
    )

    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if objects:
            # Get selection coordinates
            obj = objects[0]  # First drawn object
            left = int(obj["left"])
            top = int(obj["top"])
            width = int(obj["width"])
            height = int(obj["height"])

            # Crop and show the image
            cropped_img = img.crop((left, top, left + width, top + height))
            st.image(cropped_img, caption="Cropped Image", use_column_width=True)
