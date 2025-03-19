import streamlit as st
import numpy as np
import cv2
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("📸 Screenshot Cropper")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Show Original Image
    st.image(image, caption="Original Image", use_column_width=True)

    # Create a drawable canvas
    st.subheader("✏️ Draw a selection to crop")
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  
    stroke_width=3,
    stroke_color="red",
    background_image=img_array,  # FIX: Directly pass numpy array
    update_streamlit=True,
    width=image.width,
    height=image.height,
    drawing_mode="rect",
    key="canvas",
)


    # Process crop
    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if objects:
            obj = objects[0]  # First drawn rectangle
            x, y, w, h = int(obj["left"]), int(obj["top"]), int(obj["width"]), int(obj["height"])

            cropped_img = img_array[y:y+h, x:x+w]  # Crop
            cropped_pil = Image.fromarray(cropped_img)

            st.subheader("🖼 Cropped Image")
            st.image(cropped_pil, caption="Cropped Image", use_column_width=True)

            # Download Button
            st.download_button(
                label="📥 Download Cropped Image",
                data=cv2.imencode(".png", cv2.cvtColor(cropped_img, cv2.COLOR_RGB2BGR))[1].tobytes(),
                file_name="cropped_image.png",
                mime="image/png",
            )
