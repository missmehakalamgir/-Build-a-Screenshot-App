import streamlit as st
from PIL import Image, ImageOps
import io
from rembg import remove

# Set Streamlit page title
st.set_page_config(page_title="Photo Editor", layout="wide")

# Sidebar for better UI
st.sidebar.title("Photo Editor Options")

# File Uploader
uploaded_image = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Main title
st.title("📸 Photo Manipulation Tool")

# Display uploaded image
if uploaded_image:
    img = Image.open(uploaded_image).convert("RGBA")
    st.image(img, caption="🖼️ Original Image", use_column_width=True)

    # Remove Background Button
    if st.sidebar.button("Remove Background"):
        try:
            img_no_bg = remove(uploaded_image.getvalue())
            img_no_bg = Image.open(io.BytesIO(img_no_bg)).convert("RGBA")
            st.image(img_no_bg, caption="🚀 Background Removed", use_column_width=True)
            img = img_no_bg  # Replace original image
        except Exception as e:
            st.error("❌ Error removing background!")

    # Upload New Background
    background_image = st.sidebar.file_uploader("Upload a New Background", type=["jpg", "jpeg", "png"])
    
    if background_image:
        new_bg = Image.open(background_image).convert("RGBA")
        new_bg = new_bg.resize(img.size)  # Resize new background
        img_alpha = img.split()[-1]  # Get transparency mask

        # Combine foreground & background
        combined_image = Image.new("RGBA", img.size)
        combined_image.paste(new_bg, (0, 0))
        combined_image.paste(img, (0, 0), img_alpha)
        
        st.image(combined_image, caption="🌟 Image with New Background", use_column_width=True)
        img = combined_image  # Replace with modified image

    # Rotate Image
    rotate_angle = st.sidebar.slider("Rotate Image", 0, 360, 0)
    if rotate_angle:
        rotated_img = img.rotate(rotate_angle, expand=True)
        st.image(rotated_img, caption=f"🔄 Rotated {rotate_angle}°", use_column_width=True)
        img = rotated_img  # Replace with rotated image

    # Crop Image
    if st.sidebar.button("Crop Image to Square"):
        cropped_img = ImageOps.fit(img, (300, 300))
        st.image(cropped_img, caption="✂️ Cropped Image", use_column_width=True)
        img = cropped_img  # Replace with cropped image

    # Download Edited Image
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="💾 Download Image",
        data=byte_im,
        file_name="edited_image.png",
        mime="image/png"
    )

else:
    st.info("📌 Upload an image to start editing.")
