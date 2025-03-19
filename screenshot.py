import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

# Streamlit UI
st.set_page_config(page_title="Screenshot Cropper", layout="wide")
st.title("📸 Screenshot Cropper")

# Upload image
uploaded_file = st.file_uploader("📤 Upload Screenshot (PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Canvas for selection
    st.write("🎨 **Draw a selection to crop:**")
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)", 
        stroke_width=3, 
        stroke_color="red",
        background_image=img,  # Set image as background
        height=img.height, 
        width=img.width, 
        drawing_mode="rect", 
        key="canvas"
    )

    # Crop button
    if st.button("✂️ Crop Screenshot"):
        if canvas_result.json_data and "objects" in canvas_result.json_data:
            objects = canvas_result.json_data["objects"]
            if objects:
                rect = objects[0]
                cropped_img = img.crop((
                    int(rect["left"]), 
                    int(rect["top"]), 
                    int(rect["left"] + rect["width"]), 
                    int(rect["top"] + rect["height"])
                ))
                st.image(cropped_img, caption="✨ Cropped Screenshot", use_container_width=True)
            else:
                st.warning("⚠️ Please draw a selection before cropping.")
        else:
            st.warning("⚠️ No selection detected. Try again.")

# Footer
st.markdown("<p style='text-align: center;'>🚀 Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
