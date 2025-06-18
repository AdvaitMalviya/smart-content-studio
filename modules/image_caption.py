import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

def render():
    st.header("🖼️ Image-to-Caption Generator")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Caption"):
            with st.spinner("Generating caption..."):
                processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
                model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
                inputs = processor(images=image, return_tensors="pt")
                output = model.generate(**inputs)
                caption = processor.decode(output[0], skip_special_tokens=True)

                st.success("Generated Caption:")
                st.write(caption)
