import streamlit as st
import requests
from PIL import Image


'''
st.title("My mole classifier app")
#st.write("Please load your image")
param1 = st.slider('Select a number', 1, 10, 3)
param2 = st.slider('Select another number', 1, 10, 3)
#this needs to be changed with the gcp url
url = 'https://melcont-frvnbh56ia-ew.a.run.app/predict'

params = {
    'feature1': param1,  # 0 for Sunday, 1 for Monday, ...
    'feature2': param2
}
response = requests.get(url, params=params).json()
#st.text(response.json())
st.write("The mole ", str(response['prediction']))'''

#########################################################

# Title
highlighted_text_title = (
    "<span style='font-size: 35px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)


two_mode = st.selectbox('Choose How', ['Upload Image File', 'Live Capture'])

if two_mode == "Upload Image File":
    # File uploader
    st.markdown('<h4 style="color:gray;">Upload the Image :open_file_folder:</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Check the uploaded Image
    if uploaded_file is not None:
        # Read Image file
        image = Image.open(uploaded_file)
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)
        #Predict Button
        predict_button = st.button('Prediction')
        # When the Button "Prediction" is pushed >> Link it to Model
        predict_url = 'https://melcont-frvnbh56ia-ew.a.run.app/predict'
        if predict_button:
            files = {'file': uploaded_file.getvalue()}
            response = requests.post(predict_url, files=files)
            result = response.json()
            st.write("The mole is ", result["Mole_prediction"], "with probability", result["Probability"])
            '''
            predict_url = 'https://melcont-frvnbh56ia-ew.a.run.app/predict'
            #response = requests.post(predict_url, files={'img':image}, timeout=30)
            response = requests.get(predict_url, files={'img':image})
            #st.write("O/X")
            st.write("The mole is ", str(response['Mole_prediction'])) '''

elif two_mode =='Live Capture':
    st.markdown('<h4 style="color:gray;">Live Capture :movie_camera:</h4>', unsafe_allow_html=True)
    captured_picture = st.camera_input("Take a picture")
    if captured_picture:
        st.image(captured_picture, caption="Captured Image", use_column_width=True)
        #Predict Button
        predict_button = st.button('Prediction')
        # When the Button "Prediction" is pushed >> Link it to Model
        if predict_button:
            #st.write("O/X")
