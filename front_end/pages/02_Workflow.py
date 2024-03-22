import streamlit as st
import os
from PIL import Image

# Function to get the absolute path of the image file
def get_image_path(image_name):
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # Construct the path to the image
    image_path = os.path.join(current_dir, 'images', image_name)
    return image_path

# Title
highlighted_text_title = (
    "<span style='font-size: 30px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

def subpage1():
    def display_side_content(side):
        if side == "Data":
            image_path = get_image_path('small_imgs_mel_01.jpg')
            st.image(image_path, width=700)
            st.markdown("<span style=\"font-size:20px\">**Dataset**</span>", unsafe_allow_html=True)
            st.markdown("- <span style=\"font-size:18px\">Kaggle dataset from the original **HAM10000** (Human Against Machine with 10,000 Training images) dataset.</span>", unsafe_allow_html=True)
            st.markdown("📊 Source: [Kaggle Melanoma Dataset](https://www.kaggle.com/datasets/drscarlat/melanoma)")

        elif side == "Preprocessing":
            st.markdown("- <span style=\"font-size:18px\">Data augmentation for balancing the data</span>\n"
                        "- <span style=\"font-size:20px\">Reshaping of images to **224x224 pixels** for **CNN processing**, normalized</span>", unsafe_allow_html=True)
            image_path = get_image_path('training_sets.png')
            st.image(image_path, use_column_width=True)

        elif side == "Process":
            st.markdown("<span style=\"font-size:20px\">**From data to prediction**</span>", unsafe_allow_html=True)
            image_path = get_image_path('process_DIAGRAM_01.png')
            st.image(image_path, width=800)

        elif side == "Kernels":
            st.markdown("<span style=\"font-size:20px\">**what happens in the black box**</span>", unsafe_allow_html=True)
            image_path = get_image_path('kernels_01.png')
            st.image(image_path, width=800)

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

    tabs_list = ["Data", "Preprocessing", "Process", "Kernels"]
    active_tab = horizontal_tabs(tabs_list)

    if active_tab:
        display_side_content(active_tab)

# Define function to display subpage 2 content
def subpage2():
    st.header("Prediction Model")
    image_path1 = get_image_path('liri_1.png')
    st.image(image_path1, width=1000)
    image_path2 = get_image_path('liri_2.png')
    st.image(image_path2, width=1000)

# Create sidebar navigation menu
subpage = st.sidebar.radio("Workflow", ["Data", "Prediction Model"])

# Display content based on selected subpage
if subpage == "Data":
    subpage1()
elif subpage == "Prediction Model":
    subpage2()
