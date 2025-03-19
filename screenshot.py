import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

st.title("📸 Screenshot Cropper (Mouse Selection)")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    image = np.array(image)
    st.image(image, caption="Original Image", use_column_width=True)

    st.write("📌 **Drag to Select Area**")
    
    # Streamlit's built-in image selection tool
    from streamlit_cropper import st_cropper

    cropped_img = st_cropper(image, realtime_update=True, box_color="#FF4B4B")
    
    if cropped_img is not None:
        st.image(cropped_img, caption="Cropped Image", use_column_width=True)
