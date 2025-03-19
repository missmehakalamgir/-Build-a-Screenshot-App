import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import numpy as np
from PIL import Image

st.title("📸 Screenshot Cropper")

# 🖼️ Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # 🎨 Draw a selection box
    st.subheader("🎨 Draw a selection to crop:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  
        stroke_width=3,
        stroke_color="red",
        background_image=img_array,  
        update_streamlit=True,
        width=image.width,
        height=image.height,
        drawing_mode="rect",
        key="canvas",
    )

    # ✂️ Crop Image
    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if objects:
            obj = objects[0]  # First drawn rectangle
            x, y, w, h = int(obj["left"]), int(obj["top"]), int(obj["width"]), int(obj["height"])
            cropped_img = image.crop((x, y, x + w, y + h))
            st.subheader("🖼️ Cropped Image")
            st.image(cropped_img)

            # 📥 Download Cropped Image
            cropped_img.save("cropped.png")
            with open("cropped.png", "rb") as file:
                st.download_button("Download Cropped Image", file, file_name="cropped.png")

