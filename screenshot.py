import streamlit as st
from PIL import Image
import numpy as np
import cv2

# 🔹 Page Title
st.set_page_config(page_title="Screenshot Cropper", layout="centered")
st.markdown("<h1 style='text-align:center;'>✂️ Screenshot Cropper</h1>", unsafe_allow_html=True)

# 📤 Image Upload
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="📷 Uploaded Image", use_column_width=True)

    # 🎯 Get Crop Coordinates
    x1, x2 = st.slider("🔽 Select Width", 0, img.width, (0, img.width))
    y1, y2 = st.slider("🔄 Select Height", 0, img.height, (0, img.height))

    # ✂️ Crop Image
    if st.button("Crop Screenshot"):
        cropped_img = np.array(img)[y1:y2, x1:x2]
        st.image(Image.fromarray(cropped_img), caption="✨ Cropped Image", use_column_width=True)

# Footer
st.markdown("<p style='text-align:center; color:gray;'>🚀 Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
