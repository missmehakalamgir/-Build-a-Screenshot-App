import streamlit as st
import cv2
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("🖼 Screenshot Cropper with Mouse Selection")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    image = np.array(image)
    st.image(image, caption="Original Image", use_column_width=True)
    
    # Create a canvas for cropping
    st.write("### Draw a selection to crop:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Transparent fill
        stroke_width=2,
        stroke_color="#FF0000",
        background_image=Image.fromarray(image),
        update_streamlit=True,
        width=image.shape[1],
        height=image.shape[0],
        drawing_mode="rect",  # Rectangle selection mode
        key="canvas"
    )
    
    # Crop the selected area
    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if objects:
            obj = objects[0]  # Only consider the first drawn rectangle
            left = int(obj["left"])
            top = int(obj["top"])
            width = int(obj["width"])
            height = int(obj["height"])
            
            cropped_image = image[top:top+height, left:left+width]
            if cropped_image.size > 0:
                st.image(cropped_image, caption="Cropped Image", use_column_width=True)
            else:
                st.warning("Invalid crop selection. Please select a valid area.")
