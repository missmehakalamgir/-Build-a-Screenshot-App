import streamlit as st
import numpy as np
from PIL import Image
import cv2
from streamlit_drawable_canvas import st_canvas

st.title("📸 Screenshot Cropper App")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Show image with selection canvas
    st.write("🎨 **Draw a selection to crop:**")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Transparent selection box
        stroke_width=3,
        stroke_color="red",
        background_image=image,
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="rect",
        key="canvas",
    )

    # Crop the selected area
    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if len(objects) > 0:
            obj = objects[0]
            x1, y1, width, height = map(int, [obj["left"], obj["top"], obj["width"], obj["height"]])
            cropped_img = img_array[y1:y1+height, x1:x1+width]
            cropped_pil = Image.fromarray(cropped_img)

            st.image(cropped_pil, caption="🖼 Cropped Image", use_column_width=True)
        else:
            st.warning("⚠️ Please draw a selection to crop.")

