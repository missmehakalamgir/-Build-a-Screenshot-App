import streamlit as st
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("📸 Screenshot Cropper (Live Preview)")

# Upload Image
uploaded_file = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    img = img.convert("RGBA")  # ✅ Fix: Ensure correct image format
    img_array = np.array(img)

    # Show Original Image
    st.image(img, caption="🖼 Original Image", use_column_width=True)

    # Fix: Convert image to NumPy for background
    bg_image = Image.fromarray(img_array)

    # Canvas for selection
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",  
        stroke_width=3,
        stroke_color="red",
        background_image=bg_image,  # ✅ Fixed background image issue
        update_streamlit=True,
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
                x, y, w, h = max(0, x), max(0, y), min(img.width - x, w), min(img.height - y, h)

                # Crop
                cropped = img.crop((x, y, x + w, y + h))

                # Show cropped image
                st.image(cropped, caption="✅ Cropped Image", use_column_width=True)

                # Download button
                st.download_button("📥 Download Cropped Image", cropped.tobytes(), file_name="cropped.png")
            else:
                st.warning("⚠ Please draw a rectangle to select an area.")
