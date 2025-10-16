from dotenv import load_dotenv                                                  # importing all python libraries and environment from load_dotenv package, required for our application

load_dotenv()                                                                   # load the vaienv virtual environment
import base64                                                                   # syntactical library required
import streamlit as st                                                          # required for frontend code generation
import os                                                                       # operating system
import io                                                                       # input output
from PIL import Image                                                           # library to import images
import pdf2image                                                                # library to convert pdf into images
import google.generativeai as genai                                             # to use functions of google gemini ai in our app

## backend part
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))                            # to build connection with gemini using pregenerated API key

def get_gemini_response(input,pdf_cotent,prompt):                               # udf to get JD as input, resume in pdf format, & inputing a prompt to specify action to be done on the pdf
    model=genai.GenerativeModel('gemini-pro-vision')                            # gemini works with textual data but gemini-pro-vision works with image/pdf/audio/video formats
    response=model.generate_content([input,pdf_content[0],prompt])              # pdf -> images -> text and given to model in form of an array
    return response.text                                                        # the response generated from model is returned

def input_pdf_setup(uploaded_file):                                             # udf to convert pdf into an image
    if uploaded_file is not None:
        images=pdf2image.convert_from_bytes(uploaded_file.read())               # converts the PDF to image if something is uploaded (not none)

        first_page=images[0]
        img_byte_arr = io.BytesIO()                                             # converts images to bytes
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()                 # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App - (frontend part)

st.set_page_config(page_title="ATS Resume EXpert")                              # naming the app
st.header("ATS Tracking System")                                                # heading displayed on the page
input_text=st.text_area("Job Description: ",key="input")                        # takes input from field of JobDescription
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])       # upload only pdf type files in streamlit


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")                                 # user clickable buttons on app to perform the function mentioned in prompt

#submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

## Customizing the model using prompts
input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

# Actual program flow logic 

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
