import streamlit as st
from PIL import Image
import numpy as np
from streamlit_cropper import st_cropper

def main():
    st.title("📸 Screenshot Cropper")
    
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.subheader("🖼 Original Image")
        st.image(img, use_column_width=True)
        
        # Cropper
        st.subheader("✂️ Draw a selection to crop")
        cropped_img = st_cropper(img, box_color='#FF0000', aspect_ratio=None)
        
        if cropped_img:
            st.subheader("🎯 Cropped Image")
            st.image(cropped_img, use_column_width=True)
            
            # Download option
            img_bytes = np.array(cropped_img)
            img_pil = Image.fromarray(img_bytes)
            st.download_button("Download Cropped Image", img_pil.tobytes(), file_name="cropped.png", mime="image/png")

if __name__ == "__main__":
    main()
