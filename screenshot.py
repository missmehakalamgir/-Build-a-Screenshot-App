import streamlit as st
import cv2
import numpy as np
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("🖼 Screenshot Cropper")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    image = np.array(image)
    st.image(image, caption="Original Image", use_column_width=True)

    # Canvas for cropping
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=2,
        stroke_color="#FF0000",
        background_image=Image.fromarray(image),
        update_streamlit=True,
        height=image.shape[0],
        width=image.shape[1],
        drawing_mode="rect",
        key="canvas",
    )

    if canvas_result.json_data is not None:
        for obj in canvas_result.json_data["objects"]:
            if obj["type"] == "rect":
                left = int(obj["left"])
                top = int(obj["top"])
                width = int(obj["width"])
                height = int(obj["height"])

                cropped_image = image[top : top + height, left : left + width]
                st.image(cropped_image, caption="Cropped Image", use_column_width=True)
