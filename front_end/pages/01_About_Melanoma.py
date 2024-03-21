import streamlit as st
from PIL import Image

# Sidebar

st.sidebar.markdown('''
## <span style="font-size: 14px;">Jihyeong LEE</span><br><span style="font-size: 14px;">Julijana STEIMLE</span><br><span style="font-size: 14px;">Liridone ZHUGOLLI</span><br><span style="font-size: 14px;">Loredana HOREZEANU</span>
''', unsafe_allow_html=True)


# Title
highlighted_text_title = (
    "<span style='font-size: 30px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)


# Define the text with custom HTML and CSS styling
highlighted_text = (
    "<span style='font-size: 25px; color: gray;  font-family: Calibri; '>"
    "What's Melanoma?"
    "</span>"
)


# Display the rest of the text using the st.text_area function
rest_of_text = (
    "Melanoma is a kind of skin cancer that starts in the melanocytes. Melanocytes are cells that make the pigment that gives skin its color. The pigment is called melanin. Melanoma typically starts on skin that's often exposed to the sun. This includes the skin on the arms, back, face and legs. Melanoma also can form in the eyes. Rarely, it can happen inside the body, such as in the nose or throat. The exact cause of all melanomas isn't clear. Most melanomas are caused by exposure to ultraviolet light. Ultraviolet light, also called UV light, comes from sunlight or tanning lamps and beds. Limiting exposure to UV light can help reduce the risk of melanoma. The risk of melanoma seems to be increasing in people under 40, especially women. Knowing the symptoms of skin cancer can help ensure that cancerous changes are detected and treated before the cancer has spread. Melanoma can be treated successfully if it is found early."
)
st.markdown(highlighted_text, unsafe_allow_html=True)
st.text_area("▶", rest_of_text)

#IMAGE (https://docs.streamlit.io/library/api-reference/media/st.image)
st.image("images/melanoma_image.jpg") #caption='Source: '

# Page Link
st.page_link("https://www.mayoclinic.org/diseases-conditions/melanoma/symptoms-causes/syc-20374884", label="Click! for more Information", icon="👉")
