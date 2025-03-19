import streamlit as st
import cv2
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("📸 Screenshot Cropper App")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    st.subheader("🖼 Original Image")
    st.image(image, use_column_width=True)
    
    # Canvas for cropping
    st.subheader("🎨 Draw a selection to crop:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=2,
        stroke_color="#FF5733",
        background_image=image,
        update_streamlit=True,
        height=img_array.shape[0],
        width=img_array.shape[1],
        drawing_mode="rect",  # Allow rectangle selection
        key="canvas"
    )
    
    if canvas_result.json_data:
        for obj in canvas_result.json_data["objects"]:
            if obj["type"] == "rect":
                left = int(obj["left"])
                top = int(obj["top"])
                width = int(obj["width"])
                height = int(obj["height"])
                cropped_img = img_array[top:top+height, left:left+width]
                st.subheader("✂ Cropped Image")
                st.image(cropped_img, use_column_width=True)
