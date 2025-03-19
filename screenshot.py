import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.set_page_config(page_title="Screenshot Cropper", layout="wide")
st.title("📸 Screenshot Cropper")

# Upload image
uploaded_file = st.file_uploader("📤 Upload Screenshot (PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Canvas without background_image to avoid error
    st.write("🎨 **Draw a selection to crop:**")
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)", 
        stroke_width=3, 
        stroke_color="red",
        background_color="white",  # Fix: Removed background_image to prevent error
        height=400, 
        width=600, 
        drawing_mode="rect", 
        key="canvas"
    )

    # Crop button
    if st.button("✂️ Crop Screenshot"):
        if canvas_result.json_data and "objects" in canvas_result.json_data:
            objects = canvas_result.json_data["objects"]
            if objects:
                rect = objects[0]
                left = int(rect["left"])
                top = int(rect["top"])
                width = int(rect["width"])
                height = int(rect["height"])

                # Crop the uploaded image
                cropped_img = img.crop((left, top, left + width, top + height))
                st.image(cropped_img, caption="✨ Cropped Screenshot", use_container_width=True)
            else:
                st.warning("⚠️ Please draw a selection before cropping.")
        else:
            st.warning("⚠️ No selection detected. Try again.")

# Footer
st.markdown("<p style='text-align: center;'>🚀 Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
