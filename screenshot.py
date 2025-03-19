import streamlit as st
from PIL import Image, ImageOps
import io
from rembg import remove

# Title of the App
st.title("Photo Manipulation Tool")

# Upload Image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    img = Image.open(uploaded_image).convert("RGBA")
    st.image(img, caption="Original Image", use_column_width=True)

    # Remove Background
    if st.button("Remove Background"):
        img_no_bg = remove(uploaded_image.getvalue())
        img_no_bg = Image.open(io.BytesIO(img_no_bg)).convert("RGBA")
        st.image(img_no_bg, caption="Background Removed", use_column_width=True)
        img = img_no_bg  

    # Upload New Background
    background_image = st.file_uploader("Upload a New Background Image", type=["jpg", "jpeg", "png"])
    
    if background_image is not None:
        new_bg = Image.open(background_image).convert("RGBA")
        new_bg = new_bg.resize(img.size)  

        img_alpha = img.split()[-1]  
        combined_image = Image.new("RGBA", img.size)
        combined_image.paste(new_bg, (0, 0)) 
        combined_image.paste(img, (0, 0), img_alpha)  

        st.image(combined_image, caption="Image with New Background", use_column_width=True)
        img = combined_image  

    # Rotate Image
    rotate_angle = st.slider("Rotate Image", 0, 360, 0)
    if rotate_angle:
        rotated_img = img.rotate(rotate_angle, expand=True)
        st.image(rotated_img, caption=f"Rotated {rotate_angle}°", use_column_width=True)
        img = rotated_img  

    # Crop Image
    if st.button("Crop Image to Square"):
        cropped_img = ImageOps.fit(img, (300, 300))
        st.image(cropped_img, caption="Cropped Image", use_column_width=True)
        img = cropped_img  

    # Download Image
    if st.button("Download Image"):
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(label="Download Image", data=byte_im, file_name="manipulated_image.png", mime="image/png")
else:
    st.write("Please upload an image to start.")
