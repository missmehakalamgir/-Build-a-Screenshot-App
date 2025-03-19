import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("📸 Screenshot Cropper")

# Upload Image
uploaded_file = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    img_array = np.array(img)

    # Show Original Image
    st.image(img, caption="Original Image", use_container_width=True)

    # Selection Box
    x1 = st.slider("X1", 0, img.width, 10)
    y1 = st.slider("Y1", 0, img.height, 10)
    x2 = st.slider("X2", x1 + 10, img.width, img.width)
    y2 = st.slider("Y2", y1 + 10, img.height, img.height)

    # Crop Image
    if st.button("✂ Crop Image"):
        cropped = img_array[y1:y2, x1:x2]
        cropped_pil = Image.fromarray(cropped)
        st.image(cropped_pil, caption="Cropped Image", use_container_width=True)

        # Download Option
        st.download_button("📥 Download Cropped Image", cropped_pil.tobytes(), file_name="cropped.png")
