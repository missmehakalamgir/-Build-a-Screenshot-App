import streamlit as st
from PIL import Image

st.set_page_config(page_title="Screenshot Cropper", layout="wide")
st.title("📸 Screenshot Cropper")

# 🖼️ Upload Image
uploaded_file = st.file_uploader("📤 Upload Screenshot (PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="📸 Uploaded Image", use_container_width=True)

    # 🔲 Get Crop Coordinates
    st.write("✂️ **Enter crop area (in pixels):**")
    col1, col2, col3, col4 = st.columns(4)
    left = col1.number_input("Left", min_value=0, value=50)
    top = col2.number_input("Top", min_value=0, value=50)
    width = col3.number_input("Width", min_value=10, value=200)
    height = col4.number_input("Height", min_value=10, value=200)

    # ✂️ Crop Image
    if st.button("Crop Screenshot"):
        try:
            cropped_img = img.crop((left, top, left + width, top + height))
            st.image(cropped_img, caption="✨ Cropped Screenshot", use_container_width=True)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# Footer
st.markdown("<p style='text-align: center;'>🚀 Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
