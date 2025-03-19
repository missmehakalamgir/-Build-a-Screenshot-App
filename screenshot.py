import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

# App Title
st.title("📸 Screenshot Cropper App (Drag to Select)")

# Upload Image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Open Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Canvas for Selection
    st.subheader("🖱️ Drag to Select Crop Area")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Transparent Orange
        stroke_width=2,
        stroke_color="red",
        background_image=image,
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="rect",  # Rectangle Selection
        key="canvas",
    )

    # Crop Image on Selection
    if canvas_result and canvas_result["rects"]:
        rect = canvas_result["rects"][0]
        x1, y1 = int(rect["left"]), int(rect["top"])
        x2, y2 = x1 + int(rect["width"]), y1 + int(rect["height"])

        cropped_image = image.crop((x1, y1, x2, y2))
        st.image(cropped_image, caption="Cropped Image", use_column_width=True)

        # Download Button
        img_bytes = io.BytesIO()
        cropped_image.save(img_bytes, format="PNG")
        st.download_button(label="📥 Download Cropped Image",
                           data=img_bytes.getvalue(),
                           file_name="cropped_image.png",
                           mime="image/png")
