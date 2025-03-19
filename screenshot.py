import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

# 🔹 Page Config
st.set_page_config(page_title="Screenshot Cropper", layout="wide")

# 🔥 Title with Animation
st.markdown("<h1 style='text-align:center;'>📸 Screenshot Cropper</h1>", unsafe_allow_html=True)
st.write("🎨 **Upload an image, draw a selection, and crop!**")

# 📤 Image Upload
uploaded_file = st.file_uploader("Upload Screenshot (PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="📷 Uploaded Image", use_container_width=True)

    # 🎨 Canvas
    st.write("✏️ **Draw a selection to crop:**")
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)", stroke_width=3, stroke_color="red",
        background_image=img, height=img.height, width=img.width, drawing_mode="rect", key="canvas"
    )

    # ✂️ Crop Button
    if st.button("✂️ Crop Screenshot"):
        if canvas_result.json_data and len(canvas_result.json_data["objects"]) > 0:
            rect = canvas_result.json_data["objects"][0]
            left, top, width, height = int(rect["left"]), int(rect["top"]), int(rect["width"]), int(rect["height"])
            cropped_img = np.array(img)[top:top+height, left:left+width]
            st.image(Image.fromarray(cropped_img), caption="✨ Cropped Image", use_container_width=True)
        else:
            st.warning("⚠️ Draw a selection before cropping!")

# Footer with Animation
st.markdown("<p style='text-align:center; color:gray;'>🚀 Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
``
