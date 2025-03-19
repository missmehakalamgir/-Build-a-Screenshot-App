import streamlit as st
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("📸 Screenshot Cropper (Drag to Select)")

# Upload Image
uploaded_file = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    img_array = np.array(img)

    # Show Original Image
    st.image(img, caption="🖼 Original Image", use_container_width=True)

    # Canvas for selection
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",  
        stroke_width=2,
        stroke_color="red",
        background_image=img,  
        height=img.height,
        width=img.width,
        drawing_mode="rect",
        key="canvas"
    )

    # Crop Image when a rectangle is drawn
    if st.button("✂ Crop Image"):
        if canvas_result.json_data is not None:
            objects = canvas_result.json_data["objects"]
            if objects:
                rect = objects[0]  # First rectangle
                x, y, w, h = int(rect["left"]), int(rect["top"]), int(rect["width"]), int(rect["height"])

                # Crop
                cropped = img.crop((x, y, x + w, y + h))

                # Show cropped image
                st.image(cropped, caption="✅ Cropped Image", use_container_width=True)

                # Download button
                st.download_button("📥 Download Cropped Image", cropped.tobytes(), file_name="cropped.png")
            else:
                st.warning("⚠ Please draw a rectangle to select an area.")
