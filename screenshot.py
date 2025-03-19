import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import base64

# ---- UI Styling ----
st.set_page_config(page_title="Screenshot Cropper", layout="wide")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>📸 Screenshot Cropper</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload an image, draw a selection, and crop easily!</p>", unsafe_allow_html=True)

# ---- Function to Convert Image to Base64 ----
def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return f"data:image/png;base64,{base64.b64encode(buffered.getvalue()).decode()}"

# ---- Upload Screenshot ----
uploaded_file = st.file_uploader("📤 Upload Screenshot (PNG/JPG)", type=["png", "jpg", "jpeg"])
canvas_background_url = None
img = None

# ---- Show Uploaded Image & Set as Canvas Background ----
if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    canvas_background_url = image_to_base64(img)  # Convert image to base64 URL

# ---- Drawing Canvas ----
st.write("🎨 **Draw a selection to crop:**")
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)", stroke_width=3, stroke_color="blue",
    background_image=canvas_background_url, height=400, width=600, drawing_mode="rect", key="canvas",
)

# ---- Crop Button ----
if st.button("✂️ Crop Screenshot"):
    if uploaded_file and canvas_result.json_data:
        objects = canvas_result.json_data["objects"]
        if objects:
            rect = objects[0]
            cropped_img = img.crop((int(rect["left"]), int(rect["top"]), int(rect["left"] + rect["width"]), int(rect["top"] + rect["height"])))
            st.image(cropped_img, caption="✨ Cropped Screenshot", use_container_width=True)
        else:
            st.warning("⚠️ Please draw a selection before cropping.")
    else:
        st.warning("⚠️ Upload an image first.")

# ---- Footer ----
st.markdown("<p style='text-align: center; font-size: 14px;'>🚀 Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
