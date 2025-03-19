import streamlit as st
from PIL import Image, ImageOps
import io

# Streamlit App Title
st.title("Simple Photo Editors")

# Upload Image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    img = Image.open(uploaded_image)
    st.image(img, caption="Original Image", use_column_width=True)
    
    # Rotate Image
    angle = st.slider("Rotate Image", 0, 360, 0)
    rotated_img = img.rotate(angle)
    st.image(rotated_img, caption=f"Rotated {angle}°", use_column_width=True)
    
    # Grayscale Option
    if st.checkbox("Convert to Grayscale"):
        gray_img = ImageOps.grayscale(rotated_img)
        st.image(gray_img, caption="Grayscale Image", use_column_width=True)
        final_img = gray_img
    else:
        final_img = rotated_img
    
    # Download Button
    buf = io.BytesIO()
    final_img.save(buf, format="PNG")
    byte_img = buf.getvalue()
    st.download_button("Download Image", data=byte_img, file_name="edited_image.png", mime="image/png")
else:
    st.write("Upload an image to start editing!")
