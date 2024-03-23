import streamlit as st
from PIL import Image
import os

# Function to get the absolute path of the image file
def get_image_path(image_name):
    # Specify the correct directory path
    directory_path = "/mount/src/scan_your_skin/front_end/images/"
    # Construct the full path to the image
    image_path = os.path.join(directory_path, image_name)
    return image_path

# Display content based on the active tab
def display_side_content(active_tab):
    if active_tab == "About":
        # Use the function to get the correct image path for "About" tab
        image_path = get_image_path('about_1.jpg')
        st.image(image_path, width=550)
        st.markdown("""
        - <span style="font-size:larger; color: gray;">most invasive skin cancer with the highest risk of death</span>
        - <span style="font-size:larger; color: gray;">grows fast and can spread to any organ</span>
        - <span style="font-size:larger; color: gray;">high survival rate with early diagnosis but diminishes fast as melanoma progresses</span>
        """, unsafe_allow_html=True)

    elif active_tab == "Motivation":
        # Use the function to get the correct image path for "Motivation" tab
        image_path = get_image_path('survival_rate.png')
        st.image(image_path, width=700)
        st.markdown("""
        - <span style="font-size:larger; color: gray;">Accuracy rate of diagnosis: about 60% (up to 89% with dermoscopy)</span>
        - <span style="font-size:larger; color: gray;">Still challenging to diagnose early melanoma</span>
        - <span style="font-size:larger; color: gray;">Using computer-aided methods can improve diagnostic accuracy and increase survival rate of patients</span>
        """, unsafe_allow_html=True)

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

# Function to handle horizontal tabs
def horizontal_tabs(default_tabs=[], default_active_tab=0):
    selected_tab = st.session_state.get('selected_tab', default_tabs[default_active_tab])

    if not default_tabs:
        return None

    cols = st.columns(len(default_tabs))
    for index, tab_name in enumerate(default_tabs):
        with cols[index]:
            if st.button(tab_name, key=tab_name):
                selected_tab = tab_name

    st.session_state.selected_tab = selected_tab
    return selected_tab

# Define tabs and get the currently active tab
tabs_list = ["About", "Motivation"]
active_tab = horizontal_tabs(tabs_list)

# Display content for the active tab
if active_tab:
    display_side_content(active_tab)
