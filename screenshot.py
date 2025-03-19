import streamlit as st
from PIL import Image, ImageOps
import io
from rembg import remove

# Set the title of the app
st.title("Photo Manipulation Tool")

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Load the image
    img = Image.open(uploaded_image).convert("RGBA")  # Ensure image is in RGBA format
    st.image(img, caption="Original Image", use_column_width=True)

    # Step 1: Remove Background
    if st.button("Remove Background"):
        img_no_bg = remove(uploaded_image.getvalue())  # Use rembg to remove background
        img_no_bg = Image.open(io.BytesIO(img_no_bg)).convert("RGBA")  # Open as RGBA for transparency
        st.image(img_no_bg, caption="Background Removed", use_column_width=True)
        img = img_no_bg  # Replace the original image with the background-removed version

    # Step 2: Upload a New Background Image
    background_image = st.file_uploader("Upload a New Background Image", type=["jpg", "jpeg", "png"])
    
    if background_image is not None:
        new_bg = Image.open(background_image).convert("RGBA")  # Load the new background image
        new_bg = new_bg.resize(img.size)  # Resize to match the size of the original image

        # Step 3: Combine Images
        # Separate image transparency into a mask
        img_alpha = img.split()[-1]  # Extract the alpha channel (transparency mask)

        # Create a new background
        combined_image = Image.new("RGBA", img.size)  # Create a blank image

        # Paste the new background and then paste the foreground image with the alpha mask
        combined_image.paste(new_bg, (0, 0))  # Paste the new background
        combined_image.paste(img, (0, 0), img_alpha)  # Paste the image on top using the alpha mask

        st.image(combined_image, caption="Image with New Background", use_column_width=True)
        
        img = combined_image  # Replace the image with the newly combined image

    # Step 4: Rotate the image
    rotate_angle = st.slider("Rotate Image", 0, 360, 0)  # Slider for rotation angle
    if rotate_angle:
        rotated_img = img.rotate(rotate_angle, expand=True)  # Rotate with expanded canvas to avoid cropping
        st.image(rotated_img, caption=f"Image Rotated by {rotate_angle} degrees", use_column_width=True)
        img = rotated_img  # Replace the image with the rotated version

    # Step 5: Crop the image
    if st.button("Crop Image to Square"):
        cropped_img = ImageOps.fit(img, (300, 300))  # Crop the image to a square of 300x300
        st.image(cropped_img, caption="Cropped Image", use_column_width=True)
        img = cropped_img  # Replace the image with the cropped version

    # Step 6: Download the manipulated image
    if st.button("Download Image"):
        buf = io.BytesIO()
        img.save(buf, format="PNG")  # Save as PNG to preserve transparency
        byte_im = buf.getvalue()
        st.download_button(label="Download Image", data=byte_im, file_name="manipulated_image.png", mime="image/png")
else:
    st.write("Please upload an image to start.")
