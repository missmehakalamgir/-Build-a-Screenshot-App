import streamlit as st
import cv2
import numpy as np
from PIL import Image

# 🏷️ Title
st.title("📸 Screenshot Cropper App")

# 📤 Upload Image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Open Image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # 🎯 Image Dimensions
    h, w, _ = img_array.shape

    # 🖱️ Select Crop Area (X, Y, Width, Height)
    x1 = st.slider("Select X1 (Left)", 0, w, 0)
    y1 = st.slider("Select Y1 (Top)", 0, h, 0)
    x2 = st.slider("Select X2 (Right)", x1 + 10, w, w)
    y2 = st.slider("Select Y2 (Bottom)", y1 + 10, h, h)

    # 🖼️ Show Selection
    st.image(image.crop((x1, y1, x2, y2)), caption="Cropped Image")

    # 📥 Download Cropped Image
    cropped = image.crop((x1, y1, x2, y2))
    st.download_button("📥 Download Cropped Image",
                       data=cropped.tobytes(),
                       file_name="cropped_image.png",
                       mime="image/png")
