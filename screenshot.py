import streamlit as st
from PIL import Image
import io

# App Title
st.title("📸 Screenshot Cropper App")

# Upload Image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Open Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Selection Sliders
    st.subheader("Select Crop Area:")
    x1 = st.slider("Start X", 0, image.width, 0)
    y1 = st.slider("Start Y", 0, image.height, 0)
    x2 = st.slider("End X", x1 + 10, image.width, image.width)
    y2 = st.slider("End Y", y1 + 10, image.height, image.height)

    # Crop Image
    cropped_image = image.crop((x1, y1, x2, y2))
    st.image(cropped_image, caption="Cropped Image", use_column_width=True)

    # Download Button
    img_bytes = io.BytesIO()
    cropped_image.save(img_bytes, format="PNG")
    st.download_button(label="📥 Download Cropped Image",
                       data=img_bytes.getvalue(),
                       file_name="cropped_image.png",
                       mime="image/png")

