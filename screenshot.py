import streamlit as st
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("📸 Screenshot Cropper (Live Preview)")

# Upload Image
uploaded_file = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    img_array = np.array(img)

    # Show Original Image
    st.image(img, caption="🖼 Original Image", use_container_width=True)

    # Canvas for selection (Image inside canvas now)
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",  
        stroke_width=2,
        stroke_color="red",
        background_image=img,  # 🔥 FIXED: Image now shows inside selection box
        height=img_array.shape[0],
        width=img_array.shape[1],
        drawing_mode="rect",
        key="canvas"
    )

    # Crop Image when a rectangle is drawn
    if st.button("✂ Crop Image"):
        if canvas_result.json_data is not None:
            objects = canvas_result.json_data["objects"]
            if objects:
                rect = objects[0]  # First rectangle
                x, y, w, h = map(int, [rect["left"], rect["top"], rect["width"], rect["height"]])

                # Fix: Ensure coordinates are within image bounds
                x, y, w, h = max(0, x), max(0, y), min(img.width, w), min(img.height, h)

                # Crop
                cropped = img.crop((x, y, x + w, y + h))

                # Show cropped image
                st.image(cropped, caption="✅ Cropped Image", use_container_width=True)

                # Download button
                st.download_button("📥 Download Cropped Image", cropped.tobytes(), file_name="cropped.png")
            else:
                st.warning("⚠ Please draw a rectangle to select an area.")
