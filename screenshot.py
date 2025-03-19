import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import io

# 🏷️ Title
st.title("🖱️ Screenshot Cropper - Select Area with Mouse!")

# 📤 Upload Image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Open Image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # 🖼️ Display Image with Canvas
    st.write("🎨 **Draw a selection to crop:**")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Transparent Orange
        stroke_width=3,
        stroke_color="red",
        background_image=img_array,  # 🛠️ FIXED: Image as NumPy Array
        update_streamlit=True,
        height=img_array.shape[0],
        width=img_array.shape[1],
        drawing_mode="rect",
        key="canvas"
    )

    # 🎯 Crop Selection
    if canvas_result.json_data:
        objects = canvas_result.json_data["objects"]
        if len(objects) > 0:
            # Get last drawn rectangle
            obj = objects[-1]
            x, y, w, h = int(obj["left"]), int(obj["top"]), int(obj["width"]), int(obj["height"])

            # Crop Image
            cropped = image.crop((x, y, x + w, y + h))
            st.image(cropped, caption="🖼️ Cropped Image", use_column_width=True)

            # 📥 Download Cropped Image
            buf = io.BytesIO()
            cropped.save(buf, format="PNG")
            st.download_button("📥 Download Cropped Image", buf.getvalue(), "cropped_image.png", "image/png")
