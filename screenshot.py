import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

st.set_page_config(page_title="Screenshot Cropper", layout="wide")
st.title("📸 Screenshot Cropper")

# 🖼️ Upload Image
uploaded_file = st.file_uploader("📤 Upload Screenshot (PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    img = img.convert("RGBA")
    st.image(img, caption="📸 Uploaded Image", use_container_width=True)

    # 🖊️ Create Selection Canvas
    st.write("🎨 **Draw a selection to crop:**")
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)",
        stroke_width=3,
        stroke_color="red",
        background_image=img,
        height=img.height,
        width=img.width,
        drawing_mode="rect",
        key="canvas",
    )

    # ✂️ Crop the Image
    if st.button("Crop Screenshot"):
        if canvas_result.json_data is not None:
            objects = canvas_result.json_data["objects"]
            if len(objects) > 0:
                rect = objects[0]  # Taking the first rectangle drawn
                left, top = int(rect["left"]), int(rect["top"])
                width, height = int(rect["width"]), int(rect["height"])

                # Convert image to numpy array & crop
                img_array = np.array(img)
                cropped_img = img_array[top:top + height, left:left + width]

                # Convert back to PIL image
                cropped_pil = Image.fromarray(cropped_img)
                st.image(cropped_pil, caption="✨ Cropped Screenshot", use_container_width=True)
            else:
                st.warning("⚠️ Please draw a selection before cropping!")
        else:
            st.warning("⚠️ No selection detected!")

# Footer
st.markdown("<p style='text-align: center;'>🚀 Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
