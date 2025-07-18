
"""
You have a Streamlit ML Webapp code stored on Github and You want to deploy - Hugging Face Spaces is your latest option to deploy your Streamlit and Gradio ML Web Apps. This Hugging Face Tutorial shows how to set up a workflow of Streamlit Code to be deployed on Hugging Face Spaces. This workflow is going to be powered by Github Actions, Code on Github edited with Github.dev
"""

import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("Easy OCR - Extract Text from Images")

#subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit` -  hosted on 🤗 Spaces")

st.markdown("Link to the app - [image-to-text-app on 🤗 Spaces](https://huggingface.co/spaces/Amrrs/image-to-text-app)")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by @1littlecoder. Credits to 🤗 Spaces for Hosting this ")
